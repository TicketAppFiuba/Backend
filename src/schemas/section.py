from pydantic import BaseModel

class SectionSchema(BaseModel):
    time: str
    description: str

    class Config:
        orm_mode = True