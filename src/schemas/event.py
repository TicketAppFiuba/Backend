from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import date
from src.schemas.ubication import UbicationSchema
from src.schemas.section import *
from src.schemas.image import *
from src.schemas.faq import *
from src.schemas.section import *
from src.schemas.authorizer import *

class EventSchema(BaseModel):
    title: str
    category: str
    date: date
    description: str
    capacity: int = Field(None, gt=0, lt=10000)
    ubication: UbicationSchema
    agenda: Optional[List[SectionSchema]]
    authorizers: Optional[List[AuthorizerSchema]]

    class Config:
        orm_mode = True

class EventSchemaUpdate(BaseModel):
    id: int
    title: Optional[str]
    category: Optional[str]
    date: Optional[date]
    description: Optional[str]
    direction: Optional[str]
    latitude: Optional[float]
    longitude: Optional[float]
    capacity: Optional[int] = Field(None, gt=0, lt=10000)
    agenda: Optional[List[SectionSchema]] = []
    vacancies: Optional[int]
    
    class Config:
        orm_mode = True

class EventSchemaOut(BaseModel):
    id: int
    title: str
    direction: str
    capacity: int
    latitude: float
    organizer_email: str
    description: str
    category: str
    date: date
    vacancies: int
    longitude: float
    # sections: List[SectionSchema]
    
    class Config:
        orm_mode = True

class EventAllInfoSchemaOut(BaseModel):
    Event: EventSchemaOut
    Images: List[ImageSchemaOut]
    FAQ: List[FaqSchemaOut]
    # Agenda: List[SectionSchema]
    
    class Config:
        orm_mode = True

class EventAllInfoWithDistanceSchemaOut(BaseModel):
    Event: EventSchemaOut
    Images: List[ImageSchemaOut]
    FAQ: List[FaqSchemaOut]
    Distance: float
    
    class Config:
        orm_mode = True