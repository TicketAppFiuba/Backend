from src.schemas.reservation import *
from src.models.user import User
from sqlalchemy.orm import Session
from src.config.event import get
from src.config.reservation import create
from src.controllers.validations import *

def create_reservation(event_id: int, user_db: User, db: Session):
    event_db = get(event_id, db)
    check_permission_reservation(user_db, event_db, db)
    create(ReservationSchema(event_id=event_id, user_id=user_db.id), db)
    return {"detail": "Reservation created successfully"}
