from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
from schemas.project import ProjectCreate, ShowProject
from db.session import get_db
from db.repository.project import create_new_project, get_all_projects, get_project
import asyncio
from uuid import UUID


router = APIRouter()


@router.get("/", response_model=list[ShowProject])
def read_projects(db: Session = Depends(get_db)):
    projects = get_all_projects(db)
    return projects


@router.get("/{project_id}", response_model=ShowProject)
def read_project(project_id: UUID, db: Session = Depends(get_db)):
    project = get_project(project_id, db)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    return project


@router.post("/",response_model = ShowProject, status_code=status.HTTP_201_CREATED)       
def create_project(project : ProjectCreate,db: Session = Depends(get_db)):
    try:
        project = create_new_project(owner_id=project.owner_id,project=project,db=db)
        return project
    except Exception as e:
        print(e)
        return {"error": str(e)}

        