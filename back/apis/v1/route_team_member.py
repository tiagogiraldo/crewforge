from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
from schemas.team_member import TeamMemberCreate, ShowTeamMember
from db.session import get_db
from db.repository.team_member import create_new_team_member, get_teams_by_user_id
from db.repository.team_member import get_all_team_members, get_team_members_by_team
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

@router.get("/", response_model = list[ShowTeamMember])        
def read_teams_members(db: Session = Depends(get_db)):
    all_team_members = get_all_team_members(db)
    return all_team_members

@router.get("/{team_member_id}", response_model = ShowTeamMember) 
def read_team_member_by_id(team_member_id:UUID, db: Session = Depends(get_db)) :
    team_member = get_team_member(team_member_id, db)
    if not team_member:
        raise HTTPException(status_code=404, detail="User not found")
    return team_member_id

@router.get("/{team_id}", response_model = list[ShowTeamMember])
def read_team_members_by_team(team_id:UUID, db:Session = Depends(get_db)):
    team_members_by_team = get_team_members_by_team(team_id, db)
    if not team_member:
        raise HTTPException(status_code=404, detail="Team not found")
    return team_members_by_team

@router.get("/{user_id}", response_model = list[ShowTeamMember])
def read_teams_by_user_id(user_id: UUID, db:Session = Depends(get_db)):
    teams_by_user = get_teams_by_user_id(user_id, db)
    if not teams_by_user :
        raise HTTPException(status_code=404, detail="User not found")
    return teams_by_user 