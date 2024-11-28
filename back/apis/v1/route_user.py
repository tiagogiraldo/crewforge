from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
from schemas.user import UserCreate, ShowUser
from db.session import get_db
from db.repository.user import create_new_user, get_all_users, get_user 
import asyncio
from uuid import UUID

router = APIRouter()

@router.get("/", response_model=list[ShowUser])
def read_users(db: Session = Depends(get_db)):
    users = get_all_users(db)
    return users


@router.get("/{user_id}", response_model=ShowUser)
def read_user(user_id: UUID, db: Session = Depends(get_db)):
    user = get_user(user_id, db)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.post("/",response_model = ShowUser, status_code=status.HTTP_201_CREATED)       
def create_user(user : UserCreate,db: Session = Depends(get_db)):
    user = create_new_user(user=user,db=db)
    return user