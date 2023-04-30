from pydantic import BaseModel

class QRSchema(BaseModel):
    reservation_code: str