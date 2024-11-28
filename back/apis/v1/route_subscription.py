from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
from schemas.subscription import SubscriptionCreate, ShowSubscription
from db.session import get_db
from db.repository.subscription import create_new_subscription
from db.repository.subscription import get_all_subscriptions, get_subscription
from uuid import UUID
import asyncio

router = APIRouter()


@router.get("/", response_model=list[ShowSubscription])
def read_subscriptions(db: Session = Depends(get_db)):
    subscriptions = get_all_subscriptions(db)
    return subscriptions


@router.get("/{subscription_id}", response_model=ShowSubscription)
def read_subscription(subscription_id: UUID, db: Session = Depends(get_db)):
    subscription = get_subscription(subscription_id, db)
    if not subscription:
        raise HTTPException(status_code=404, detail="User not found")
    return subscription


@router.post("/",response_model = SubscriptionCreate, status_code=status.HTTP_201_CREATED)    
def create_subscription(subscription : SubscriptionCreate,db: Session = Depends(get_db)):
    try:
        subscription =  create_new_subscription(user_id=subscription.user_id, subscription=subscription, db=db)
        return subscription
    except Exception as e:
        print(e)
        return {"error": str(e)}