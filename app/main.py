from fastapi import FastAPI, UploadFile, File
from app.core.config import settings

app = FastAPI()

@app.get("/health")
def health_sync():
    return {
        "status": "ok",
        "app": settings.app_name,
        "debug": settings.debug,
        "type": "sync"
    }

ALLOWED_TYPES = {
    "image/jpeg",
    "image/png",
    "video/mp4",
    "video/webm",
}

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    if file.content_type not in ALLOWED_TYPES:
        return {"error": "Unsupported Media Type"}

    return {
        "filename": file.filename,
        "content_type": file.content_type,
        "status": "accepted",
    }