from pydantic import Basemodel
from uuid import UUID
from datetime import date, datetime

class TaskProgressCreate(Basemodel):
    name: str
    user_id: UUID
    task_assignment_id: UUID


class ShowTaskProgress(BaseModel):
    id: UUID
    progress: float   
    updated_at: datetime
    user_id: UUID
    task_assignment_id: UUID
    