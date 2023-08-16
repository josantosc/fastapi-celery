from celery.app.task import Task


class TaskExemplo(Task):
    name = "Task.exemplo"
    queue = "LOCAL-queue"

    def run(self, **kwargs):
        print("TESTE")
