from fastapi import HTTPException
from sqlalchemy.orm import Session
from src.config import reservation
from src.config import complaint
from src.models.user import User
from src.schemas.reservation import *
from src.schemas.complaint import *
from src.controllers.validator import validator
from src.config import favorite
    
def check_create_reservation(reservationSchema: ReservationCreateSchema, user_db: User, db: Session):
    validator.validate_user_reservation(reservationSchema, db)
    reservation_db = reservation.getByUserAndEvent(user_db.id, reservationSchema.event_id, db)
    if reservation_db is not None:
        raise HTTPException(status_code=403, detail="Event already booked.")
    return ReservationSchema(**reservationSchema.dict(), user_id=user_db.id) 

def check_create_complaint(complaintSchema: ComplaintCreateSchema, user_db: User, db: Session):
    validator.validate_user_complaint(complaintSchema, db)
    complaint_db = complaint.getByUserAndEvent(user_db.id, complaintSchema.event_id, db)
    if complaint_db is not None:
        raise HTTPException(status_code=403, detail="Complaint already report.")
    return ComplaintSchema(**complaintSchema.dict(), user_id=user_db.id)    

def check_add_favorite_event(user_id: int, event_id: int, db: Session):
    event_db = validator.validate_event(event_id, db)
    favorite_db = favorite.getByUserAndEvent(user_id, event_id, db)
    if favorite_db is not None:
        raise HTTPException(status_code=403, detail="The event has already been added.")
    return event_db

def check_delete_favorite_event(user_id: int, event_id: int, db: Session):
    validator.validate_event(event_id, db)
    favorite_db = favorite.getByUserAndEvent(user_id, event_id, db)
    if favorite_db is None:
        raise HTTPException(status_code=403, detail="The event is not includes in the favorite event list.")
    return favorite_db
       