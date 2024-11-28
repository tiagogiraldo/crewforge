from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
from schemas.subscription_status import ShowSubscriptionStatus
from db.session import get_db
from db.repository.subscription_status import get_all_subscriptions_status, get_subscription_status
from uuid import UUID
import asyncio

router = APIRouter()


@router.get("/", response_model=list[ShowSubscriptionStatus])
def read_subscriptions_status(db: Session = Depends(get_db)):
    subscriptions_status = get_all_subscriptions_status(db)
    return subscriptions_status


@router.get("/{subscription_status_id}", response_model=ShowSubscriptionStatus)
def read_subscription_status(subscription_status_id: UUID, db: Session = Depends(get_db)):
    subscription_status = get_subscription_status(subscription_status_id, db)
    if not subscription_status:
        raise HTTPException(status_code=404, detail="Status not found")
    return subscription_status
