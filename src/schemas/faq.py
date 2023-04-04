from pydantic import BaseModel

class FaqSchema(BaseModel):
    question: str
    answer: str
    event_id: int
    
    class Config:
        orm_mode = True

class FaqUpdateSchema(BaseModel):
    event_id: int
    id: int
    question: str
    answer: str

    class Config:
        orm_mode = True

class FaqDeleteSchema(BaseModel):
    id: int
    event_id: int

class FaqSchemaOut(BaseModel):
    question: str
    answer: str
    
    class Config:
        orm_mode = True
