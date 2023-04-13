from pydantic import BaseModel

class ReservationSchema(BaseModel):
    event_id: int
    user_id: int
    