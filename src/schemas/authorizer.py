from pydantic import BaseModel
from typing import Optional

class AuthorizerSchema(BaseModel):
    email: str

    class Config:
        orm_mode = True

class EventOutSchema(BaseModel):
    id: int
    title: str
    direction: str
    capacity: int
    vacancies: int
    description: str
    link: Optional[str]

    class Config:
        orm_mode = True