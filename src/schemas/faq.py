from pydantic import BaseModel
from typing import Optional

class FAQSchema(BaseModel):
    event_id: int
    question: str
    response: str

    class Config:
        orm_mode = True

class FAQCreateSchema(BaseModel):
    question: str
    response: str

    class Config:
        orm_mode = True


class FAQUpdateSchema(BaseModel):
    id: int
    event_id: int
    question: Optional[str]
    response: Optional[str]

    class Config:
        orm_mode = True

class FAQDeleteSchema(BaseModel):
    id: int
    event_id: int

class FaqSchemaOut(BaseModel):
    question: Optional[str]
    response: Optional[str]

    class Config:
        orm_mode = True
