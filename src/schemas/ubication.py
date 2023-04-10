from pydantic import BaseModel

class UbicationSchema(BaseModel):
    direction: str
    latitude: int
    longitude: int

    class Config:
        orm_mode = True