from sqlalchemy.orm import Session
from src.models.event import Event
from sqlalchemy import func, cast, Float
from src.models.attendance import Attendance
from src.models.reservation import Reservation

def attendance_rate(event_id: int, db: Session):
    #return db.query(Event.title, func.count(Reservation.event_id).label("att"), Event.capacity)\
    #         .join(Reservation, Attendance.reservation_id == Reservation.id)\
    #         .join(Event, Reservation.event_id == Event.id)\
    #         .filter(Event.id == event_id)\
    #         .group_by(Reservation.event_id)\
    #         .first()
    return 1

def reservation_rate(event_id: int, db: Session):
    return db.query(Event.id, Event.title, (cast(Event.vacancies, Float)/Event.capacity).label("reservation_ratio"))\
             .filter(Event.id == event_id)\
             .first()

def attendance_per_hour(event_id: int, db: Session):
    return db.query(Attendance.hour, func.count(Attendance.hour).label("attendances"))\
             .filter(Attendance.reservation_id == Reservation.id)\
             .filter(Reservation.event_id == event_id)\
             .group_by(Attendance.hour)\
             .order_by(Attendance.hour)\
             .all()

# SELECT Event.vacancies/Event.capacity
# FROM Event
# WHERE Event.id == event_id

# SELECT Assistance.hour, func.count(Assistance.hour).label("assistance")
# FROM Assistance
# GROUP_BY Assitance.hour
# ORDER_BY Assistance.hour

# SELECT COUNT(Reservation.event_id)/Event.capacity, Event.id
# FROM Assistance, Reservation, Event
# WHERE Assistance.reservation_id == Reservation.id
# AND Reservation.event_id == Event.id
# GROUP BY Reservation.event_id