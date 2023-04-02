from pydantic import BaseModel

class UbicationSchema(BaseModel):
    direction: str
    latitude: str
    length: str

    class Config:
        orm_mode = True