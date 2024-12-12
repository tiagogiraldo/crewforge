from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
from schemas.task import TaskCreate, ShowTask
from db.session import get_db
from db.repository.task import create_new_task, get_all_tasks, get_task
from uuid import UUID

router = APIRouter()

@router.get("/", response_model=list[ShowTask])
def read_tasks(db:Session = Depends(get_db)):
    tasks = get_all_tasks(db)
    return tasks

@router.get("/{task_id}", response_model=ShowTask)
def read_task(task_id: UUID, db: Session = Depends(get_db)):
    task = get_task(task_id, db)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task



@router.post("/", response_model = ShowTask, status_code = status.HTTP_201_CREATED)
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    try:
        task = create_new_task(owner_id= task.user_id, project_id = task.projec_id, task = task, db=db)
        return task
    except Exception as e:
        print(e)
        return{"error": str(e)}