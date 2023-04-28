from fastapi import HTTPException
from sqlalchemy.orm import Session
from src.config import reservation
from src.config import event
from src.config import complaint
from src.models.user import User
from src.schemas.reservation import *
from src.schemas.complaint import *

def validate_event(event_id: int, db: Session):
    event_db = event.get(event_id, db)
    if event_db is None:
        raise HTTPException(status_code=404, detail="Event not exist.")
    return event_db

def check_permission_reservation(reservationSchema: ReservationCreateSchema, user_db: User, db: Session):
    event_db = validate_event(reservationSchema.event_id, db)
    reservation_db = reservation.getByUserAndEvent(user_db.id, event_db.id, db)
    if reservation_db is not None:
        raise HTTPException(status_code=403, detail="Event already booked.")
    if reservationSchema.tickets > 4:
        raise HTTPException(status_code=403, detail="The maximum number of tickets is four.")
    if reservationSchema.tickets <= 0:
        raise HTTPException(status_code=403, detail="The number of tickets must be greater than zero.")
    if event_db.vacancies - reservationSchema.tickets < 0:
        raise HTTPException(status_code=403, detail="The number of tickets exceeds the capacity of the event.")
    return ReservationSchema(event_id=reservationSchema.event_id, user_id=user_db.id, tickets=reservationSchema.tickets)

def check_permission_complaint(complaintSchema: ComplaintSchema, user_db: User, db: Session):
    event_db = validate_event(complaintSchema.event_id, db)
    complaint_db = complaint.getByUserAndEvent(user_db.id, event_db.id, db)
    if complaint_db is not None:
        raise HTTPException(status_code=403, detail="Complaint already report.")
    return ComplaintSchema(event_id=complaintSchema.event_id, user_id=user_db.id, category=complaintSchema.category, description=complaintSchema.description)
