from sqlalchemy.orm import Session
from schemas.task import TaskAssignmentCreate, ShowTaskAssignment 
from db.models.task import Task
from db.models.subscription_status import Subscription_Status
from db.models.user import User
from db.models.task_assignment import Task_Assignment
from fastapi import HTTPException
from uuid import UUID
import asyncio

def create_new_task_assignment(owner_id: UUID, task_id:UUID, task_assignment:TaskAssignmentCreate):
    existing_owner = db.query(User).filter(User.id == owner_id).first()
    existing_task = db.query(Task).filter(Task.is == task_id).first()

    if existing_owner.active == False:
        raise HTTPException(status_code=401, detail="User unauthoried")

    if existing_task is None:
        raise HTTPException(status_code=404, detail="Task not found")

    i