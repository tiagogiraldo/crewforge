from pydantic import BaseModel, Field, PositiveFloat
from datetime import date, datetime
from uuid import UUID


class SubscriptionCreate(BaseModel):
    subscription_type: str
    user_id: UUID


class ShowSubscription(BaseModel):
    id: UUID
    subscription_type: str
    payment: float
    payment_date: datetime
    expiration_date: datetime
    user_id: UUID    