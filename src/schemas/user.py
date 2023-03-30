from pydantic import BaseModel
from typing import List

class UserSchema(BaseModel):
    email: str
    name: str

    class Config:
        orm_mode = True