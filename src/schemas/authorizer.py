from pydantic import BaseModel
from datetime import date

class AuthorizerSchema(BaseModel):
    email: str

    class Config:
        orm_mode = True

class EventOutSchema(BaseModel):
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
    link: str

    class Config:
        orm_mode = True