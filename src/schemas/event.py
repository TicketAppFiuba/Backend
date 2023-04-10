from pydantic import BaseModel
from typing import Optional
from datetime import date
from src.schemas.ubication import UbicationSchema
from src.schemas.image import *
from src.schemas.faq import *
from typing import List

class EventSchema(BaseModel):
    title: str
    category: str
    date: date
    description: str
    capacity: int
    vacancies: int
    ubication: UbicationSchema
    pic: str
    class Config:
        orm_mode = True

class EventSchemaUpdate(BaseModel):
    id: int
    title: Optional[str]
    category: Optional[str]
    date: Optional[date]
    description: Optional[str]
    direction: Optional[str]
    latitude: Optional[int]
    longitude: Optional[int]
    capacity: Optional[int]
    vacancies: Optional[int]
    
    class Config:
        orm_mode = True

class EventSchemaOut(BaseModel):
    id: int
    title: str
    direction: str
    capacity: str
    latitude: int
    organizer_email: str
    description: str
    category: str
    date: date
    vacancies: int
    longitude: int
    
    class Config:
        orm_mode = True

class EventAllInfoSchemaOut(BaseModel):
    Event: EventSchemaOut
    Images: List[ImageSchemaOut]
    FAQ: List[FaqSchemaOut]
    class Config:
        orm_mode = True