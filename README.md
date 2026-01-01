# AI Generated Media Detection Platform

Asynchronous backend service for analyzing images and videos for AI-generated content.

The project focuses on backend architecture and task-based processing.
![img.png](img.png)
---

## Current Status

Early backend architecture stage.

Implemented:

* File upload API
* Task ID generation
* In-memory task status tracking
* Task status polling endpoint

No background processing or persistent storage is implemented yet.

---

## API

### Upload file

`POST /upload`

Creates a new task.

```json
{
  "task_id": "uuid",
  "status": "pending"
}
```

### Get task status

`GET /status/{task_id}`

```json
{
  "task_id": "uuid",
  "status": "pending"
}
```

---

## Architecture

* Task lifecycle abstraction
* Centralized task status management
* Clear separation between API and task logic

---

## Stack

* Python
* FastAPI

---
