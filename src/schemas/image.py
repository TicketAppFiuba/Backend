from pydantic import BaseModel
from typing import List

class ImageSchema(BaseModel):
    link: str

    class Config:
        orm_mode = True