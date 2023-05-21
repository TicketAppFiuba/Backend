from sqlalchemy.orm import Session
from src.models.event import Event
from sqlalchemy import func, cast, Float
from src.models.attendance import Attendance
from src.models.reservation import Reservation

def attendance_date(event_id: int, db: Session):
    return db.query(func.count(Event.id).label("attendances"),
                    (Event.capacity-func.count(Event.id)).label("availability"),
                    (cast(func.count(Event.id), Float)/Event.capacity).label("attendance_ratio"))\
             .join(Reservation, Reservation.event_id == Event.id)\
             .join(Attendance, Attendance.reservation_id == Reservation.id)\
             .filter(Event.id == event_id)\
             .group_by(Event.id)\
             .first()

def reservation_date(event_id: int, db: Session):
    return db.query(Event.capacity, 
                    Event.vacancies,
                    (Event.capacity-Event.vacancies).label("occupancy"),
                    (cast(Event.capacity-Event.vacancies, Float)/Event.capacity).label("reservation_ratio"))\
             .filter(Event.id == event_id)\
             .first()

def attendance_per_hour(event_id: int, db: Session):
    return db.query(Attendance.hour, func.count(Attendance.hour).label("attendances"))\
             .filter(Attendance.reservation_id == Reservation.id)\
             .filter(Reservation.event_id == event_id)\
             .group_by(Attendance.hour)\
             .order_by(Attendance.hour)\
             .all()
