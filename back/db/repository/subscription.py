from sqlalchemy.orm import Session
from schemas.subscription import SubscriptionCreate
from db.models.subscription import Subscription
from db.models.user import User
from db.models.subscription_status import Subscription_Status
from datetime import datetime, timedelta
from fastapi import HTTPException
from uuid import UUID
import asyncio

def create_new_subscription(user_id: UUID, subscription: SubscriptionCreate, db: Session):
    existing_user = db.query(User).filter(User.id == user_id).first()
    if existing_user is None:
        raise HTTPException(status_code=404, detail="User not found")


    if subscription.subscription_type not in ['M', 'Y']:
        raise ValueError("Invalid subscription type")

    if subscription.subscription_type == 'M':
        payment = 120.00
        delta = timedelta(30)
    elif subscription.subscription_type == 'Y':
        payment = 1_100.00
        delta = timedelta(365)

    db_subscription = Subscription(
        payment = payment,
        subscription_type=subscription.subscription_type,  
        payment_date= datetime.now(),
        expiration_date = datetime.now() + delta,
        user_id=existing_user.id  
    )

    db.add(db_subscription)
    db.commit() 
    db.refresh(db_subscription)


    subscription_status = db.query(Subscription_Status).filter(Subscription_Status.user_id == user_id).first()
    if subscription_status is None:
        subscription_status = Subscription_Status(
            is_active=True,
            expiration_date=db_subscription.expiration_date,
            user_id=user_id
        )
        db.add(subscription_status)
    else:
        subscription_status.is_active = True
        subscription_status.expiration_date = db_subscription.expiration_date
        db.add(subscription_status)

    db.commit()
    db.refresh(subscription_status)    
    return db_subscription

def get_all_subscriptions(db: Session):
    return db.query(Subscription).all()

def get_subscription(subscription_id: UUID, db: Session):
    return db.query(Subscription).filter(Subscription.id == subscription_id).first()