from pydantic import BaseModel

class ImageSchema(BaseModel):
    event_id: int
    link: str

    class Config:
        orm_mode = True

class ImageCreateSchema(BaseModel):
    link: str

    class Config:
        orm_mode = True

class ImageUpdateSchema(BaseModel):
    id: int
    link: str

    class Config:
        orm_mode = True

class ImageDeleteSchema(BaseModel):
    id: int

    class Config:
        orm_mode = True

class ImageSchemaOut(BaseModel):
    link: str

    class Config:
        orm_mode = True