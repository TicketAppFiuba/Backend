from pydantic import BaseModel

class UserSchema(BaseModel):
    email: str
    name: str

    class Config:
        orm_mode = True