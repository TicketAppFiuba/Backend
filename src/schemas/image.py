from pydantic import BaseModel

class ImageSchema(BaseModel):
    event_id: int
    link: str

    class Config:
        orm_mode = True

class ImageUpdateSchema(BaseModel):
    event_id: int
    id: int
    link: str

    class Config:
        orm_mode = True

class ImageDeleteSchema(BaseModel):
    id: int
    event_id: int