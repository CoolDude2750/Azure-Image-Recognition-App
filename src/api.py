from fastapi import FastAPI, UploadFile, File, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, JSONResponse
from src.vision_client import VisionClient

app = FastAPI()
client = VisionClient()

templates = Jinja2Templates(directory="src/templates/")

# Home page (upload form)
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
    "upload.html",
    {"request": request}
)


# UI upload handler (returns HTML with results)
@app.post("/upload")
async def upload_image(request: Request, file: UploadFile = File(...)):
    image_bytes = await file.read()
    result = client.analyze_bytes(image_bytes)

    caption = result.caption.text if result.caption else None
    tags = [t["name"] for t in result.tags.get("values", [])]
    objects = [o["tags"][0] for o in result.objects.get("values", []) if o.get("tags")]

    return templates.TemplateResponse(
        "upload.html",
        {
            "request": request,
            "caption": caption,
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
    tags = [t["name"] for t in result.tags.get("values", [])]
    objects = [o["tags"][0] for o in result.objects.get("values", []) if o.get("tags")]

    return JSONResponse({
        "caption": caption,
        "tags": tags,
        "objects": objects
    })
