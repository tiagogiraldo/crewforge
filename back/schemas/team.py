from pydantic import BaseModel, Field, PositiveFloat
from datetime import date, datetime
from uuid import UUID


class TeamCreate(BaseModel):
    name: str
    project_id: UUID


class ShowTeam(BaseModel)    :
    id: UUID
    name: str
    is_active: bool
    created_at: datetime
    updated_at:datetime
    project_id: UUID
    
    class Config():  
        from_attributes = True