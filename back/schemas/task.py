from pydantic import BaseModel
from uuid import UUID
from datetime import date, datetime

class TaskCreate(BaseModel):
    name: str
    user_id: UUID
    project_id: UUID


class ShowTask(BaseModel):
    id: UUID
    name: str
    status: str
    is_active: bool
    created_at: datetime
    updated_at: datetime
    user_id: UUID
    project_id: UUID
