import base64
import io
import json
import os
import uuid
from pathlib import Path

import httpx
from fastapi import FastAPI, File, Form, HTTPException, UploadFile
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from PIL import Image, ImageOps, UnidentifiedImageError

ROOT = Path(__file__).resolve().parent.parent
STYLES = json.loads((ROOT / "skills/styles.json").read_text())
OUTPUT = Path(os.environ.get("POSTER_OUTPUT_DIR", str(ROOT / ".runtime/generated")))
OUTPUT.mkdir(parents=True, exist_ok=True)
MAX_BYTES = 15 * 1024 * 1024
Image.MAX_IMAGE_PIXELS = 24_000_000
app = FastAPI(title="Memory Studio", version="1.0.0")
app.mount("/static", StaticFiles(directory=ROOT / "app/static"), name="static")


@app.get("/")
def index():
    return FileResponse(ROOT / "app/static/index.html")


@app.get("/api/styles")
def styles():
    return [{k: v for k, v in s.items() if k != "prompt"} for s in STYLES]


@app.get("/api/health")
def health():
    return {"status": "ok", "generation_configured": bool(os.environ.get("OPENAI_API_KEY"))}


@app.post("/api/generate")
async def generate(image: UploadFile = File(...), style: str = Form(...), title: str = Form("")):
    selected = next((s for s in STYLES if s["id"] == style), None)
    if not selected:
        raise HTTPException(400, "Unknown style.")
    title = title.strip()
    if len(title) > 100:
        raise HTTPException(400, "Title must be 100 characters or fewer.")
    data = await image.read(MAX_BYTES + 1)
    if not data or len(data) > MAX_BYTES:
        raise HTTPException(413, "Upload a non-empty image up to 15 MB.")
    try:
        with Image.open(io.BytesIO(data)) as source:
            if source.format not in {"JPEG", "PNG", "WEBP"}:
                raise ValueError("Unsupported format")
            source.load()
            photo = ImageOps.exif_transpose(source).convert("RGB")
            photo.thumbnail((2048, 2048))
            upload = io.BytesIO()
            photo.save(upload, format="PNG")
    except (UnidentifiedImageError, OSError, ValueError, Image.DecompressionBombError, Image.DecompressionBombWarning):
        raise HTTPException(400, "Please upload a valid JPG, PNG, or WebP image.")
    key = os.environ.get("OPENAI_API_KEY")
    if not key:
        raise HTTPException(503, "Generation is not configured. Set OPENAI_API_KEY on the server.")
    prompt = selected["prompt"] + " Portrait composition. The final export is 3:4; keep all important content within the central 3:4 safe area."
    prompt += (" Use this exact title as visible lettering: " + json.dumps(title)) if title else " Do not add a headline."
    try:
        async with httpx.AsyncClient(timeout=240) as client:
            response = await client.post(
                "https://api.openai.com/v1/images/edits",
                headers={"Authorization": f"Bearer {key}"},
                data={"model": os.environ.get("POSTER_IMAGE_MODEL", "gpt-image-1"), "prompt": prompt,
                      "size": "1024x1536", "quality": "medium", "n": "1"},
                files={"image": ("photo.png", upload.getvalue(), "image/png")},
            )
        if response.status_code != 200:
            if response.status_code == 429:
                raise HTTPException(429, "Generation limit reached. Check API quota and try again later.")
            raise HTTPException(502, "The image provider rejected the request. Check server API credentials and model access.")
        generated = base64.b64decode(response.json()["data"][0]["b64_json"], validate=True)
        with Image.open(io.BytesIO(generated)) as result:
            result.load()
            # Provider portrait sizes differ from 3:4; crop the prompted safe area deterministically.
            poster = ImageOps.fit(result.convert("RGB"), (1080, 1440), method=Image.Resampling.LANCZOS)
    except httpx.TimeoutException:
        raise HTTPException(504, "Generation timed out. Please try again.")
    except (httpx.HTTPError, KeyError, IndexError, ValueError, OSError):
        raise HTTPException(502, "The image provider returned an unusable result. Please try again.")
    name = uuid.uuid4().hex + ".png"
    poster.save(OUTPUT / name, "PNG")
    return {"image_url": f"/api/images/{name}", "download_url": f"/api/images/{name}?download=true", "width": 1080, "height": 1440}


@app.get("/api/images/{name}")
def get_image(name: str, download: bool = False):
    if len(name) != 36 or not name.endswith(".png") or any(c not in "0123456789abcdef" for c in name[:-4]):
        raise HTTPException(404, "Image not found.")
    path = OUTPUT / name
    if not path.is_file():
        raise HTTPException(404, "Image not found.")
    return FileResponse(path, media_type="image/png", filename="memory-poster.png" if download else None)
