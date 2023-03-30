from pydantic import BaseModel
from typing import Optional, List
from datetime import date
from src.schemas.image import ImageSchema

class EventSchema(BaseModel):
    img: List[ImageSchema]
    date: date
    description: str
    organizer: str
    tickets: int 

    class Config:
        orm_mode = True
