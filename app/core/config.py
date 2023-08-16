import os
from pydantic_settings import BaseSettings
from decouple import config


class Settings(BaseSettings):
    ENV_SERVER: str = "ENV_SERVER"
    APPLICATION_NAME: str = "fastapi-celery"

    class Config:
        case_sensitive = True
        env_file = os.path.expanduser("~/.env")

CELERY = {
    "celery_broker_url": config("CELERY_BROKER_URL"),
    "result_back_end": config("CELERY_BROKER_URL"),
    "task_time_limit": config("CELERYD_TASK_TIME_LIMIT", default=60),
    "task_ignore_result": False,
    "timezone": "America/Sao_Paulo",
    "celery_enable_utc": True,
    "task_sent_event": True,
    "task_acks_late": True,
    "worker_perfetch_multiplier": 1,
    "task_compression ": "gzip",
    "broker_connection_retry_on_startup": config("BROKER_CONNECTION_RETRY_ON_STARTUP", default=True)
}
APPLICATION_NAME = config('APPLICATION_NAME', default='groot-arji')

settings = Settings()