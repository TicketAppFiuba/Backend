from fastapi import HTTPException
from sqlalchemy.orm import Session
from src.config import image, event, faq, reservation, user
from src.models.event import Event
from src.schemas.image import *
from src.schemas.faq import *
from src.schemas.reservation import *

def validate_event(event_id: int, db: Session):
    event_db = event.get(event_id, db)
    if event_db is None:
        raise HTTPException(status_code=404, detail="Event not exist.")
    return event_db

def validate_image(image_id: int, db: Session):
    image_db = image.get(image_id, db)
    if image_db is None:
        raise HTTPException(status_code=404, detail="Image not exist.")
    return image_db

def validate_faq(faq_id: int, db: Session):
    faq_db = faq.get(faq_id, db)
    if faq_db is None:
        raise HTTPException(status_code=404, detail="FAQ not exist.")   
    return faq_db

def validate_reservation(code: str, db: Session):
    reservation_db = reservation.get(code, db)
    if reservation_db is None:
        raise HTTPException(status_code=404, detail="La reserva no existe.")
    return reservation_db

def validate_user(email: str, db: Session):
    user_db = user.get(email, db)
    if user_db is None:
        raise HTTPException(status_code=404, detail="User not exist.")
    return user_db

def validate_tickets(tickets: int, event_db: Event):
    if tickets > 4 or tickets <= 0:
        raise HTTPException(status_code=403, detail="The number of tickets is invalid.")
    if event_db.vacancies - tickets < 0:
        raise HTTPException(status_code=403, detail="The number of tickets exceeds the capacity of the event.")
    
def validate_reservation_by(schema: ReservationSchema, db: Session):
    validate_tickets(schema.tickets, validate_event(schema.event_id, db))