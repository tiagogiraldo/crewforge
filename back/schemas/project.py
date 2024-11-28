from pydantic import BaseModel, Field, PositiveFloat
from datetime import date, datetime
from uuid import UUID


class ProjectCreate(BaseModel):
    name: str
    owner_id: UUID


class ShowProject(BaseModel)    :
    id: UUID
    name: str
    is_active: bool
    created_at: datetime
    updated_at:datetime
    owner_id: UUID
    
    class Config():  
        from_attributes = True