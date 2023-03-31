from pydantic import BaseModel
from typing import Optional, List
from datetime import date
from src.schemas.image import ImageSchema
from src.schemas.ubication import UbicationSchema

class EventSchema(BaseModel):
    title: str
    category: str
    images: List[ImageSchema]
    date: date
    description: str
    tickets: int 
    ubication: UbicationSchema
    
    class Config:
        orm_mode = True

class EventSchemaOut(BaseModel):
    id: int
    date: date
    description: str
    tickets: int
    organizer: str

    class Config:
        orm_mode = True