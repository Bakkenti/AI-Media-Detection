from celery import Celery

celery_app = Celery(
    "ai_media_detection",
    broker="redis://localhost:6379/0",
)
