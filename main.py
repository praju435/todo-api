from fastapi import FastAPI
from pydantic import BaseModel

app =  FastAPI()

tasks = []

class Task(BaseModel):
    title: str
    completed: bool = False

@app.get("/")
def home():
    return {"message": "welcome to Todo API"}

@app.post("/tasks")
def create_task(task: Task):
    tasks.append(task)
    return {"task created successfully": task}

@app.get("/tasks")
def get_tasks():
    return tasks

@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    if task_id >= len(tasks) or task_id < 0:
        return{"message" : "task not found"}
    return tasks[task_id]

@app.put("/tasks/{task_id}")
def update_task(task_id:int , task:Task):
    if task_id >= len(tasks) or task_id < 0:
            return{"message" : "task not found"}
    tasks[task_id] = task
    return {"message": "task updated successfully", "task": task}

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    if task_id >= len(tasks) or task_id < 0:
        return{"message" : "task not found"}
    tasks.pop(task_id)
    return {"message": "task deleted successfully"}