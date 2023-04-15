from fastapi import HTTPException
from sqlalchemy.orm import Session
from src.config.reservation import *
from src.config.event import *
from src.models.user import User
from src.schemas.reservation import *

def validate_event(event_id: int, db: Session):
    event_db = get(event_id, db)
    if event_db is None:
        raise HTTPException(status_code=404, detail="Event not exist.")
    return event_db

def check_permission_reservation(reservation: ReservationCreateSchema, user_db: User, db: Session):
    event_db = validate_event(reservation.event_id, db)
    reservation_db = getByUserAndEvent(user_db.id, event_db.id, db)
    if reservation_db is not None:
        raise HTTPException(status_code=403, detail="Event already booked.")
    if reservation.tickets > 4:
        raise HTTPException(status_code=403, detail="The maximum number of tickets is four.")
    if event_db.vacancies - reservation.tickets < 0:
        raise HTTPException(status_code=403, detail="The number of tickets exceeds the capacity of the event.")
    return ReservationSchema(event_id=reservation.event_id, user_id=user_db.id, tickets=reservation.tickets)