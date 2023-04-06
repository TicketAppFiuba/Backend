from pydantic import BaseModel
from typing import Optional
from datetime import date
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
    latitude: Optional[int]
    length: Optional[int]
    capacity: Optional[int]
    vacancies: Optional[int]
    
    class Config:
        orm_mode = True

class EventSchemaOut(BaseModel):
    id: int
    title: str
    description: str
    organizer: str
    category: str
    date: date
    capacity: int
    vacancies: int
    ubication: UbicationSchema
    
    class Config:
        orm_mode = True
