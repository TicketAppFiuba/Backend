from pydantic import BaseModel
from typing import Optional

class ComplaintSchema(BaseModel):
    event_id: int
    user_id: int
    category: str
    description: str

    class Config:
        orm_mode = True

class ComplaintCreateSchema(BaseModel):
    event_id: int
    category: str
    description: str

    class Config:
        orm_mode = True

class ComplaintQuerySchema(BaseModel):
    category: Optional[str]
    