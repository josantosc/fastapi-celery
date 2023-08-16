import locale

from celery import Celery
from app.core.config import CELERY, APPLICATION_NAME
from app.tasks import task_registry

locale.setlocale(locale.LC_ALL, "pt_BR.UTF-8")

app = Celery(APPLICATION_NAME, tasks=task_registry, config_source=CELERY)


app.conf.beat_schedule = {
    "task.exemplo": {
        "task": "tasks.exemplo",
        "schedule": 30.0
    }
}
