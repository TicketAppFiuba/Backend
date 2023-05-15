from pydantic import BaseModel

class NotificationSchema(BaseModel):
    title: str
    description: str

    class Config:
        orm_mode = True