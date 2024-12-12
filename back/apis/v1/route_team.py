from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
from schemas.team import TeamCreate, ShowTeam
from db.session import get_db
from db.repository.team import create_new_team, get_all_teams
import asyncio
from uuid import UUID


router = APIRouter()


@router.post("/",response_model = ShowTeam, status_code=status.HTTP_201_CREATED)       
def create_team(team : TeamCreate,db: Session = Depends(get_db)):
    try:
        team = create_new_team(project_id=team.project_id,team=team,db=db)
        return team
    except Exception as e:
        print(e)
        return {"error": str(e)}


@router.get("/", response_model=list[ShowTeam])        
def read_teams(db: Session = Depends(get_db)):
    teams = get_all_teams(db)
    return teams

@router.get("/{team_id}", response_model=ShowTeam)    
def read_team(team_id: UUID, db: Session = Depends(get_db)):
    team = get_team(team_id, db)
    if not team:
        raise HTTPException(status_code=404, detail="Team not found")
    return team