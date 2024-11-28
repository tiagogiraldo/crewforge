from sqlalchemy.orm import Session
from db.models.user import User
from db.models.subscription_status import Subscription_Status
from datetime import datetime, timedelta
from fastapi import HTTPException
from uuid import UUID
import asyncio


def get_all_subscriptions_status(db: Session):
    return db.query(Subscription_Status).all()

def get_subscription_status(subscription_status_id: UUID, db: Session):
    return db.query(Subscription_Status).filter(Subscription_Status.id == subscription_status_id).first()
