from fastapi import HTTPException
from sqlalchemy.orm import Session
from src.config import reservation
from src.config import complaint
from src.models.user import User
from src.schemas.reservation import *
from src.schemas.complaint import *
from src.controllers.validator import validator
    
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
