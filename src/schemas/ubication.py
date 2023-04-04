from pydantic import BaseModel

class UbicationSchema(BaseModel):
    direction: str
    latitude: int
    length: int

    class Config:
        orm_mode = True