from pathlib import Path
from fastapi import FastAPI, UploadFile, File, Request
from starlette.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, JSONResponse
from src.vision_client import VisionClient

app = FastAPI()
client = VisionClient()

BASE_DIR = Path(__file__).resolve().parent
templates = Jinja2Templates(directory=BASE_DIR / "templates")

# Home page (upload form)
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")


# UI upload handler (returns HTML with results)
@app.post("/upload")
async def upload_image(request: Request, file: UploadFile = File(...)):
    image_bytes = await file.read()
    result = client.analyze_bytes(image_bytes)

    caption = result.caption.text if result.caption else None
    caption_confidence = getattr(result.caption, "confidence", None) if result.caption else None
    tags = [
        {
            "name": t.get("name"),
            "confidence": round(t.get("confidence", 0), 2)
        }
        for t in result.tags.get("values", []) if t.get("name")
    ]
    objects = []
    for o in result.objects.get("values", []):
        if not o.get("tags"):
            continue
        first_tag = o["tags"][0]
        obj_name = first_tag.get("name")
        obj_confidence = round(first_tag.get("confidence", 0), 2)
        if obj_name:
            objects.append({"name": obj_name, "confidence": obj_confidence})

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "caption": caption,
            "caption_confidence": caption_confidence,
            "tags": tags,
            "objects": objects
        }
    )


# Optional: JSON API endpoint (useful for testing)
@app.post("/analyze")
async def analyze_image(file: UploadFile = File(...)):
    image_bytes = await file.read()
    result = client.analyze_bytes(image_bytes)

    caption = result.caption.text if result.caption else None
    caption_confidence = getattr(result.caption, "confidence", None) if result.caption else None
    tags = [
        {
            "name": t.get("name"),
            "confidence": round(t.get("confidence", 0), 2)
        }
        for t in result.tags.get("values", []) if t.get("name")
    ]
    objects = []
    for o in result.objects.get("values", []):
        if not o.get("tags"):
            continue
        first_tag = o["tags"][0]
        obj_name = first_tag.get("name")
        obj_confidence = round(first_tag.get("confidence", 0), 2)
        if obj_name:
            objects.append({"name": obj_name, "confidence": obj_confidence})

    return JSONResponse({
        "caption": caption,
        "caption_confidence": caption_confidence,
        "tags": tags,
        "objects": objects
    })
