from pydantic import BaseModel

class QRSchema(BaseModel):
    reservation_id: int