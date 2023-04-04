from pydantic import BaseModel
from typing import Optional

class QuerySchema(BaseModel):
    title: Optional[str]
    category: Optional[str]
    min_price: Optional[str]
    max_price: Optional[int]
    
    class Config:
        orm_mode = True