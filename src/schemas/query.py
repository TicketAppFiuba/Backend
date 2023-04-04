from pydantic import BaseModel
from typing import Optional

class QuerySchema(BaseModel):
    title: Optional[str]
    category: Optional[str]
    
    class Config:
        orm_mode = True