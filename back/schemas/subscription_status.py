from pydantic import BaseModel, Field, PositiveFloat
from datetime import date, datetime
from uuid import UUID

class SubscriptionStatus(BaseModel):
    is_active: bool
    expiration_date: datetime
    user_id: UUID

class ShowSubscriptionStatus(BaseModel):
    id: UUID
    is_active: bool
    expiration_date: datetime
    user_id: UUID    