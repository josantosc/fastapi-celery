from celery.app.registry import TaskRegistry

from app.tasks.exemplo import TaskExemplo

task_registry = TaskRegistry()
task_registry.register(TaskExemplo)
