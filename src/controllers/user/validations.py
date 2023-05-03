from fastapi import HTTPException
from sqlalchemy.orm import Session
from src.config import reservation
from src.config import event
from src.config import complaint
from src.models.user import User
from src.models.event import Event
from src.schemas.reservation import *
from src.schemas.complaint import *

def validate_event(event_id: int, db: Session):
    event_db = event.get(event_id, db)
    if event_db is None:
        raise HTTPException(status_code=404, detail="Event not exist.")
    return event_db
    
def validate_reservation(schema: ReservationSchema, db: Session):
    reservation_db = reservation.getByUserAndEvent(schema.user_id, schema.event_id, db)
    if reservation_db is not None:
        raise HTTPException(status_code=403, detail="Event already booked.")
    return schema 

def validate_complaint(schema: ComplaintSchema, db: Session):
    complaint_db = complaint.getByUserAndEvent(schema.user_id, schema.event_id, db)
    if complaint_db is not None:
        raise HTTPException(status_code=403, detail="Complaint already report.")
    return schema    

def validate_tickets(tickets: int, event_db: Event):
    if tickets > 4 or tickets <= 0:
        raise HTTPException(status_code=403, detail="The number of tickets is invalid.")
    if event_db.vacancies - tickets < 0:
        raise HTTPException(status_code=403, detail="The number of tickets exceeds the capacity of the event.")
    
def check_permission_reservation(reservationSchema: ReservationCreateSchema, user_db: User, db: Session):
    event_db = validate_event(reservationSchema.event_id, db)
    validate_tickets(reservationSchema.tickets, event_db)
    return validate_reservation(ReservationSchema(**reservationSchema.dict(), user_id=user_db.id), db)

def check_permission_complaint(complaintSchema: ComplaintCreateSchema, user_db: User, db: Session):
    validate_event(complaintSchema.event_id, db)
    return validate_complaint(ComplaintSchema(**complaintSchema.dict(), user_id=user_db.id), db)
