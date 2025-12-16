from pydantic import BaseModel

class Task(BaseModel):
    """
    Task model to represent a task.
    """
    id: int
    name: str
    description: str
    completed: bool = False