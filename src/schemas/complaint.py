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