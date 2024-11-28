from sqlalchemy.orm import Session
from datetime import datetime
from schemas.user import UserCreate
from db.models.user import User
from db.models.subscription_status import Subscription_Status
from core.hashing import Hasher
import asyncio
from uuid import UUID
from fastapi import HTTPException

def create_new_user(user:UserCreate,db:Session):
    existing_user = db.query(User).filter(User.username == user.username).first()
    if existing_user is not None:
        raise HTTPException(status_code=400, detail="Username already exists")

    new_user = User(
        first_name = user.first_name,
        last_name = user.last_name,
        username = user.username,
        email = user.email,
        password = Hasher.get_password_hash(user.password),
        is_active = True,
        is_superuser = False
        )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    subscription_status = Subscription_Status(
        is_active = False,
        expiration_date = datetime.now(), 
        user_id = new_user.id
    )
    db.add(subscription_status)
    db.commit()
    db.refresh(subscription_status)

    return new_user

def get_all_users(db: Session):
    return db.query(User).all()

def get_user(user_id: UUID, db: Session):
    return db.query(User).filter(User.id == user_id).first()
