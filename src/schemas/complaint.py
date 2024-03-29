from pydantic import BaseModel
from typing import Optional
from datetime import date

class ComplaintSchema(BaseModel):
    event_id: int
    user_id: int
    category: str
    description: str

    class Config:
        orm_mode = True

class ComplaintPerUserSchema(BaseModel):
    Complaint: ComplaintSchema
    title: str
    class Config:
        orm_mode = True

class UserSchema(BaseModel):
    email: str
    firebase_token: Optional[str]
    id: int
    login: bool
    name: str
    suspended: bool

    class Config:
        orm_mode = True

class ComplaintUsersSchema(BaseModel):
    id: int
    User: UserSchema

    class Config:
        orm_mode = True

class ComplaintCreateSchema(BaseModel):
    event_id: int
    category: str
    description: str

    class Config:
        orm_mode = True

class ComplaintQuerySchema(BaseModel):
    category: Optional[str]
    date_init: Optional[date]
    date_end: Optional[date]
    
    class Config:
        orm_mode = True