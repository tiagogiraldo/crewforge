from sqlalchemy.orm import Session
from schemas.team_member import TeamMemberCreate
from db.models.team import Team
from db.models.user import User
from db.models.team_member import Team_Member
from db.models.subscription_status import Subscription_Status
from fastapi import HTTPException
from uuid import UUID
import asyncio



def create_new_team_member(owner_id: UUID, user_id: UUID, team_id: UUID, team_member: TeamMemberCreate, db: Session):
    owner_team = db.query(User).filter(User.id == owner_id).first()
    subscription_status = db.query(Subscription_Status).filter(Subscription_Status.user_id == owner_team.id).first()
    user_check = db.query(User).filter(Team_Member.user_id == user_id).first()    
    existing_team = db.query(Team).filter(Team.id == team_id).first()
    
    if user_check:
        raise HTTPException(status_code=400, detail="Member already exist")       

    if existing_team is None:
        raise HTTPException(status_code=400, detail="Team doesn't exist")       

    if subscription_status.is_active:
        new_team_member = Team_Member(
            role=team_member.role,  
            user_id=team_member.user_id,
            team_id=team_member.team_id
        )

        db.add(new_team_member)
        db.commit()
        db.refresh(new_team_member)
    else:
        raise HTTPException(status_code=403, detail="User without permission")
    
    return new_team_member

def get_all_team_members(db: Session):
    return db.query(Team_Member).all()

def get_team_member(team_member_id: UUID, db: Session):
    return db.query(Team_Member).filter(Team_Member.id == team_member_id).first()

def get_team_members_by_team(team_id: UUID, db:Session):
    return db.query(Team_Member).filter(Team_Member.team_id == team_id)


def get_teams_by_user_id(user_id: UUID, db:Session):
    return db.query(Team_Member).filter(Team_Member.user_id == user_id)

    