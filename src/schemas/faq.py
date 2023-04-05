from pydantic import BaseModel
from typing import Optional

class FAQSchema(BaseModel):
    event_id: int
    question: str
    response: str

class FAQUpdateSchema(BaseModel):
    id: int
    event_id: int
    question: Optional[str]
    response: Optional[str]

class FAQDeleteSchema(BaseModel):
    question_id: int
    event_id: int