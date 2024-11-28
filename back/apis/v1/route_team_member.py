from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
from schemas.team_member import TeamMemberCreate, ShowTeamMember
from db.session import get_db
from db.repository.team_member import create_new_team_member
import asyncio
from uuid import UUID


router = APIRouter()


@router.post("/",response_model = ShowTeamMember, status_code=status.HTTP_201_CREATED)       
def create_team_member(team_member : TeamMemberCreate,db: Session = Depends(get_db)):
    try:
        team_member = create_new_team_member(
            owner_id=team_member.owner_id,
            user_id=team_member.user_id,
            team_id=team_member.team_id,
            team_member=team_member,
            db=db)
        return team_member
    except Exception as e:
        print(e)
        return {"error": str(e)}