from celery import Celery
from config import REDIS_URL


celery = Celery(
    "fastapi_project",
    broker=REDIS_URL,
    backend=REDIS_URL,
)

celery.conf.update(
    task_serializer="json",
    result_serializer="json",
    accept_content=["json"],
    timezone="UTC",
    # Run tasks synchronously in-process (no Redis broker needed in development)
    task_always_eager=True,
    task_eager_propagates=True,
)
