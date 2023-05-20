from pydantic import BaseModel
from datetime import date

class AttendanceOutSchema(BaseModel):
    reservation_id: int
    title: str
    name: str
    hour: str
    date: date