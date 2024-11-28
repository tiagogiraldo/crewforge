from pydantic import BaseModel, Field, PositiveFloat
from datetime import date, datetime
from uuid import UUID


class TeamMemberCreate(BaseModel):
    owner_id: UUID
    role: str
    user_id: UUID
    team_id: UUID


class ShowTeamMember(BaseModel)    :
    id: UUID
    role: str
    user_id: UUID
    team_id: UUID

    
    class Config():  
        from_attributes = True