from pydantic import BaseModel

class UbicationSchema(BaseModel):
    direction: str
    latitude: float
    longitude: float

    class Config:
        orm_mode = True