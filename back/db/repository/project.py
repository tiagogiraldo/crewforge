from sqlalchemy.orm import Session
from schemas.project import ProjectCreate
from db.models.project import Project
from db.models.subscription_status import Subscription_Status
from db.models.user import User
from fastapi import HTTPException
from uuid import UUID
import asyncio



def create_new_project(owner_id: UUID, project: ProjectCreate, db: Session):
    existing_user = db.query(User).filter(User.id == owner_id).first()
    subscription_status = db.query(Subscription_Status).filter(Subscription_Status.user_id == owner_id).first()
    
    if existing_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    if subscription_status.is_active:
        new_project = Project(
            name=project.name,  
            owner_id=existing_user.id
        )

        db.add(new_project)
        db.commit()
        db.refresh(new_project)
    else:
        raise HTTPException(status_code=403, detail="User without permission")
    
    return new_project

def get_all_projects(db: Session):
    return db.query(Project).all()

def get_project(project_id: UUID, db: Session):
    return db.query(Project).filter(Project.id == project_id).first()