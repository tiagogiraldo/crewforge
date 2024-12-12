from sqlalchemy.orm import Session
from schemas.task import TaskCreate
from db.models.task import Task
from db.models.project import Project
from db.models.subscription_status import Subscription_Status
from db.models.user import User
from fastapi import HTTPException
from uuid import UUID
import asyncio



def create_new_task(owner_id: UUID, project_id: UUID, task: TaskCreate, db: Session):
    existing_user = db.query(User).filter(User.id == owner_id).first()
    existing_project = db.query(Project).filter(Project.id == project_id).first()
    existing_owner = db.query(Project).filter(Project.owner_id == existing_user).first()
    subscription_status = db.query(Subscription_Status).filter(Subscription_Status.user_id == owner_id).first()

    if existing_project is None:
        raise HTTPException(status_code=404, detail="Project not found")

    if existing_owner == False:
        raise HTTPException(status_code=401, detail="User unauthorized")
    
    if subscription_status.is_active:
        new_project = Task(
            name = task.name,
            project_id= existing_project
        )
        db.add(new_task)
        db.commit()
        db.refresh(new_task)
    else:
        raise HTTPException(stasu_code=403, detail="User without permission")
    
    return new_task


def get_all_tasks(db: Session):
    return  db.query(Task).all()


def get_task(task_id: UUID, db: Session):
    return db.query(Task).filter(Task.id == task_id).first()

        