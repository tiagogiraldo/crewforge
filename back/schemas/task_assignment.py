from pydantic import Basemodel
from uuid import UUID
from datetime import date, datetime

class TaskAssignmentCreate(Basemodel):
    name: str
    user_id: UUID
    task_id: UUID


class ShowTaskAssignment(BaseModel):
    id: UUID
    name: str
    status: str
    is_active: bool
    assigned_at: datetime
    updated_at: datetime
    user_id: UUID
    task_id: UUID
