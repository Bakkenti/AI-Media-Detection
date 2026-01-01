from fastapi import FastAPI, UploadFile, File, HTTPException
from app.core.config import settings
from pathlib import Path
from app.core.utils import generate_task_id
from app.core.tasks import tasks, STATUS_PENDING

app = FastAPI()

UPLOAD_DIR = Path("app/storage/uploads/")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)


@app.get("/health")
def health_sync():
    return {
        "status": "ok",
        "app": settings.app_name,
        "debug": settings.debug,
        "type": "sync"
    }

@app.get("/status/{task_id}")
def get_task_status(task_id: str):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")

    return {
        "task_id": task_id,
        "status": tasks[task_id],
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

    task_id = generate_task_id()

    tasks[task_id] = STATUS_PENDING

    file_path = UPLOAD_DIR.joinpath(f"{task_id}_{file.filename}")
    with open(file_path, "wb") as f:
        while chunk := await file.read(1024 * 1024):
            f.write(chunk)

    return {
        "task_id": task_id,
        "filename": file.filename,
        "content_type": file.content_type,
        "status": "saved",
    }