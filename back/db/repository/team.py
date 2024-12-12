from sqlalchemy.orm import Session
from schemas.team import TeamCreate
from db.models.team import Team
from db.models.project import Project
from db.models.user import User
from db.models.subscription_status import Subscription_Status
from fastapi import HTTPException
from uuid import UUID
import asyncio



def create_new_team(project_id: UUID, team: TeamCreate, db: Session):
    existing_project = db.query(Project).filter(Project.id == project_id).first()
    print("porject: ", existing_project)
    existing_user = db.query(User).filter(User.id == existing_project.owner_id).first()
    print("user:", existing_user)
    subscription_status = db.query(Subscription_Status).filter(Subscription_Status.user_id == existing_user.id).first()
    
    if existing_project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    
    if subscription_status.is_active:
        new_team = Team(
            name=team.name,  
            project_id=existing_project.id
        )

        db.add(new_team)
        db.commit()
        db.refresh(new_team)
    else:
        raise HTTPException(status_code=403, detail="User without permission")
    
    return new_team

def get_all_teams(db:Session):
    return db.query(Team).all()

def get_user(team_id: UUID, db: Session):
    return db.query(Team).filter(Team.id == team_id).first()