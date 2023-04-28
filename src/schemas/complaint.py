from pydantic import BaseModel

class ComplaintSchema(BaseModel):
    event_id: int
    category: str
    description: str

    class Config:
        orm_mode = True