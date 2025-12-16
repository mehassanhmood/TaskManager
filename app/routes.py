from fastapi import APIRouter, HTTPException
from app.models import Task

router = APIRouter()

# In-memory task storage
tasks = {}

@router.post("/tasks", response_model=Task)
def create_task(task: Task):
    """
    Create a new task.
    """
    if task.id in tasks:
        raise HTTPException(status_code=400, detail="Task ID already exists")
    tasks[task.id] = task
    return task

@router.get("/tasks", response_model=list[Task])
def list_tasks():
    """
    List all tasks.
    """
    return list(tasks.values())

@router.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int):
    """
    Get a task by ID.
    """
    task = tasks.get(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    """
    Delete a task by ID.
    """
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")
    del tasks[task_id]
    return {"message": "Task deleted"}