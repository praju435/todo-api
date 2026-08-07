from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud
from .database import get_db
from .crud import create_task, get_task, get_tasks, update_task, delete_task
from .schemas import TaskCreate, TaskResponse


router = APIRouter()


@router.post("/tasks", response_model=TaskResponse)
def create_task(
    task: TaskCreate,
    db: Session = Depends(get_db)
):
    return crud.create_task(db, task)

@router.get("/tasks", response_model=list[TaskResponse])
def get_tasks(
    db: Session = Depends(get_db)
):
    return crud.get_tasks(db)

@router.get("/task/{task_id}", response_model=TaskResponse)
def get_task(
    task_id: int,
    db: Session = Depends(get_db)
):
    return crud.get_task(db, task_id)

    if task is None:
        raise HTTPException(status_code=404, details="Task not found")
    return task

@router.put("/task{task_id}", response_model=TaskResponse)
def put_task(
    task_id: int,
    task: TaskCreate,
    db: Session =  Depends(get_db)
):
    updated_task = crud.update_task(db, task_id, task)
    if updated_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return updated_task

@router.delete("/task{task_id}")
def delete_task(
    task_id: int,
    db: Session = Depends(get_db)
):
    result = crud.delete_task(db, task_id)
    if not result:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"message": "Task deleted successfully"}