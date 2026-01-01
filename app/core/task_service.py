from app.core.tasks import tasks
from app.core.task_status import TaskStatus

def create_task(task_id: str):
    tasks[task_id] = TaskStatus.pending

def get_task_status(task_id: str) -> TaskStatus | None:
    return tasks.get(task_id)

def set_task_status(task_id: str, status: TaskStatus):
    tasks[task_id] = status
