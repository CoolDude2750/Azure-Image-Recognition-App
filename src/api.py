import logging
from pathlib import Path
from fastapi import FastAPI, UploadFile, File, Request, HTTPException
from starlette.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, JSONResponse
from src.vision_client import VisionClient

# Configure logging for diagnostics
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()
MAX_IMAGE_BYTES = 10 * 1024 * 1024
ALLOWED_IMAGE_TYPES = {"image/jpeg", "image/png", "image/bmp", "image/gif", "image/webp"}

try:
    client = VisionClient()
    logger.info("VisionClient initialized successfully")
except Exception as e:
    logger.error(f"Failed to initialize VisionClient: {type(e).__name__}: {e}")
    client = None

BASE_DIR = Path(__file__).resolve().parent
templates = Jinja2Templates(directory=BASE_DIR / "templates")


def _require_client() -> VisionClient:
    if client is None:
        raise HTTPException(status_code=503, detail="Vision service is not configured.")
    return client


async def _read_image(file: UploadFile) -> bytes:
    if file.content_type not in ALLOWED_IMAGE_TYPES:
        raise HTTPException(status_code=415, detail="Upload a supported image file.")

    image_bytes = await file.read(MAX_IMAGE_BYTES + 1)
    if not image_bytes:
        raise HTTPException(status_code=400, detail="The uploaded image is empty.")
    if len(image_bytes) > MAX_IMAGE_BYTES:
        raise HTTPException(status_code=413, detail="The image must be 10 MB or smaller.")
    return image_bytes


def _format_result(result) -> dict:
    caption = result.caption.text if result.caption else None
    caption_confidence = getattr(result.caption, "confidence", None) if result.caption else None
    tags = [
        {"name": tag.get("name"), "confidence": round(tag.get("confidence", 0), 2)}
        for tag in result.tags.get("values", [])
        if tag.get("name")
    ]
    objects = []
    for detected_object in result.objects.get("values", []):
        detected_tags = detected_object.get("tags", [])
        if not detected_tags:
            continue
        first_tag = detected_tags[0]
        if first_tag.get("name"):
            objects.append({
                "name": first_tag["name"],
                "confidence": round(first_tag.get("confidence", 0), 2),
            })

    return {
        "caption": caption,
        "caption_confidence": caption_confidence,
        "tags": tags,
        "objects": objects,
    }

# Home page (upload form)
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")


# UI upload handler (returns HTML with results)
@app.post("/upload")
async def upload_image(request: Request, file: UploadFile = File(...)):
    try:
        vision_client = _require_client()
        image_bytes = await _read_image(file)
        result = vision_client.analyze_bytes(image_bytes)
    except HTTPException as exc:
        return templates.TemplateResponse(
            request=request,
            name="index.html",
            context={"error": exc.detail},
            status_code=exc.status_code,
        )
    except Exception as e:
        logger.error("Error analyzing image: %s: %s", type(e).__name__, e)
        return templates.TemplateResponse(
            request=request,
            name="index.html",
            context={"error": "Failed to analyze image. Please try again."},
            status_code=502,
        )

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context=_format_result(result),
    )


# Optional: JSON API endpoint (useful for testing)
@app.post("/analyze")
async def analyze_image(file: UploadFile = File(...)):
    vision_client = _require_client()
    image_bytes = await _read_image(file)
    try:
        result = vision_client.analyze_bytes(image_bytes)
    except Exception as e:
        logger.error("Error analyzing image: %s: %s", type(e).__name__, e)
        raise HTTPException(status_code=502, detail="Failed to analyze image.") from e

    return JSONResponse(_format_result(result))
