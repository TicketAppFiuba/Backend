from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class ReservationSchema(BaseModel):
    event_id: int
    user_id: int
    tickets: int

class ReservationCreateSchema(BaseModel):
    event_id: int
    tickets: int

class ReservationOutSchema(BaseModel):
    id: int
    title: str
    direction: str
    capacity: int
    latitude: float
    organizer_email: str
    description: str
    category: str
    date: datetime
    state: str
    vacancies: int
    longitude: float
    link: Optional[str]
    favorite: Optional[bool]
    code: Optional[str]
    
    class Config:
        orm_mode = True