from fastapi import HTTPException
from sqlalchemy.orm import Session
from src.config.reservation import *
from src.config.event import *
from src.models.user import User

def validate_event(event_id: int, db: Session):
    event_db = get(event_id, db)
    if event_db is None:
        raise HTTPException(status_code=404, detail="Event not exist.")
    return event_db

def check_permission_reservation(event_id: int, user_db: User, db: Session):
    event_db = validate_event(event_id, db)
    reservation_db = getByUserAndEvent(user_db.id, event_db.id, db)
    if reservation_db is not None:
        raise HTTPException(status_code=404, detail="Not permission.")