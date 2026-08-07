from sqlalchemy.orm import Session
from .models import Task
from .schemas import TaskCreate



def create_task(db: Session, task:TaskCreate):
    db_task = Task(
    title=task.title,
    completed=task.completed,
    description=task.description
  )

    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def get_task(db: Session, task_id: int):
    task = db.query(Task).filter(Task.id == task_id).first()
    return task

def get_tasks(db: Session):
    tasks = db.query(Task).all()
    return tasks

def update_task(db: Session, task_id: int, task: TaskCreate):
    db_task = db.query(Task).filter(Task.id == task_id).first()
    if db_task:
        db_task.title = task.title
        db_task.completed = task.completed
        db_task.description = task.description
        db.commit()
        db.refresh(db_task)
        return db_task
    else: 
        return None


def delete_task(db: Session, task_id: int):
    db_task = db.query(Task).filter(Task.id == task_id).first()
    if db_task:
        db.delete(db_task)
        db.commit()
        return ("Task deleted successfully")
    else:
        return ("Task not found")


  