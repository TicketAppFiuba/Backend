from sqlalchemy.orm import Session
from src.models.attendance import Attendance
from src.models.user import User
from src.models.event import Event
from src.models.reservation import Reservation
from datetime import datetime

def register(reservation_id: int, db: Session):
    attendance_db = Attendance(reservation_id=reservation_id,
                               date=datetime.now().date(),
                               hour=datetime.now().strftime("%H:%M"))
    db.add(attendance_db)
    db.commit()
    db.refresh(attendance_db)
    return attendance_db

def getFromEvent(event_id: int, db: Session):
    return db.query(Attendance.date, Attendance.hour, Attendance.reservation_id, Event.title, User.name)\
             .join(Reservation, Attendance.reservation_id == Reservation.id)\
             .join(Event, Reservation.event_id == Event.id)\
             .join(User, Reservation.user_id == User.id)\
             .filter(Event.id == event_id)\
             .all()