from sqlalchemy.orm import Session
from src.models.calendar import Calendar
from src.models.event import Event

def create(event_id: int, user_id: int, db: Session):
    calendar_db = Calendar(event_id=event_id, user_id=user_id)
    db.add(calendar_db)
    db.commit()
    db.refresh(calendar_db)
    return calendar_db

def delete(calendar_db: Calendar, db: Session):
    db.delete(calendar_db)
    db.commit()
    
def getAllFromUser(user_id: int, db: Session):
    return db.query(Event).join(Calendar).filter(Calendar.user_id == user_id).all()

def getByUserAndEvent(user_id: int, event_id: int, db: Session):
    return db.query(Calendar).filter(Calendar.user_id == user_id).filter(Calendar.event_id == event_id).first()
