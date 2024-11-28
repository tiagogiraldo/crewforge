from pydantic import BaseModel,EmailStr, Field
from uuid import UUID

class UserCreate(BaseModel):
    first_name: str
    last_name: str
    username: str
    email : EmailStr
    password : str = Field(..., min_length=8)


class ShowUser(BaseModel):
    id: UUID
    first_name: str
    last_name: str
    username: str    
    email : EmailStr
    is_active : bool

    class Config():  
        from_attributes = True