from pydantic import BaseModel

class AuthorizerSchema(BaseModel):
    email: str

    class Config:
        orm_mode = True