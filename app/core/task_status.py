from enum import Enum

class TaskStatus(str, Enum):
    pending = "pending"
    processing = "processing"
    done = "done"
    error = "error"

tasks: dict[str, TaskStatus] = {}