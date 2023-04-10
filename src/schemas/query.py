from pydantic import BaseModel
from typing import Optional
from src.schemas.ubication import UbicationSchema

class QuerySchema(BaseModel):
    title: Optional[str]
    category: Optional[str]
    ubication: Optional[UbicationSchema] = UbicationSchema(direction="-", latitude=0, longitude=0)
    
    class Config:
        orm_mode = True