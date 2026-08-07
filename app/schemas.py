from pydantic import BaseModel, ConfigDict

class TaskCreate(BaseModel):
    title: str
    completed: bool = False
    description: str = ""

class TaskResponse(BaseModel):
    id: int
    title: str
    completed: bool
    description: str

    model_config = ConfigDict(from_attributes=True)