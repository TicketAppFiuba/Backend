from pydantic import BaseModel
from typing import Optional, List
from datetime import date
from src.schemas.image import ImageSchema

class EventSchema(BaseModel):
    images: List[ImageSchema]
    date: date
    description: str
    tickets: int 

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