from pydantic import BaseModel

class CoordinateSchema(BaseModel):
    latitude: float
    longitude: float
    
    class Config:
        orm_mode = True