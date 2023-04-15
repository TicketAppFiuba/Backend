from src.schemas.reservation import *
from src.models.user import User
from sqlalchemy.orm import Session
from src.config import reservation
from src.controllers.user.validations import *

def create_reservation(event_id: int, user_db: User, db: Session):
    check_permission_reservation(event_id, user_db, db)
    reservation.create(ReservationSchema(event_id=event_id, user_id=user_db.id), db)
    return {"detail": "Reservation created successfully"}
