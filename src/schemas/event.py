from pydantic import BaseModel
from typing import Optional, List
from datetime import date
from src.schemas.image import ImageSchema
from src.schemas.ubication import UbicationSchema

class EventSchema(BaseModel):
    title: str
    category: str
    date: date
    description: str
    capacity: int
    vacancies: int
    ubication: UbicationSchema
    
    class Config:
        orm_mode = True

class EventSchemaUpdate(BaseModel):
    id: int
    title: Optional[str]
    category: Optional[str]
    date: Optional[date]
    description: Optional[str]
    direction: Optional[str]
    latitude: Optional[str]
    length: Optional[str]
    capacity: Optional[int]
    vacancies: Optional[int]
    
    class Config:
        orm_mode = True

class EventSchemaOut(BaseModel):
    id: int
    date: date
    description: str
    tickets: int
    organizer: str
    price: int
    
    class Config:
        orm_mode = True