from sqlalchemy.orm import Session
from src.models.user import User
from src.config import calendar
from src.controllers.user import permissions
from src.config import calendar

def add_calendar(event_id: int, user_db: User, db: Session):
    permissions.check_add_calendar_event(user_db.id, event_id, db)
    calendar.create(event_id, user_db.id, db)
    return {"detail": "The event was added successfully."}

def delete_calendar(event_id: int, user_db: User, db: Session):
    calendar_db = permissions.check_delete_calendar_event(user_db.id, event_id, db)
    calendar.delete(calendar_db, db)
    return {"detail": "The event was deleted succesfully."}

def get_calendar(user_db: User, db: Session):
    return calendar.getAllFromUser(user_db.id, db)
