from pydantic import BaseModel

class QRSchema(BaseModel):
    reservation_code: str
    event_id: int