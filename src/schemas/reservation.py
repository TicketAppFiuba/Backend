from pydantic import BaseModel

class ReservationSchema(BaseModel):
    event_id: int
    user_id: int
    tickets: int

class ReservationCreateSchema(BaseModel):
    event_id: int
    tickets: int