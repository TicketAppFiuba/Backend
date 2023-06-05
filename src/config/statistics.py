from sqlalchemy.orm import Session
from src.models.event import Event
from sqlalchemy import func, cast, Float
from src.models.attendance import Attendance
from src.models.reservation import Reservation
from src.schemas.statistics import QueryDistributionSchema

def attendance_date(event_id: int, db: Session):
    return db.query(func.sum(Attendance.tickets).label("attendances"),
                    (Event.capacity-func.sum(Attendance.tickets)).label("availability"),
                    (cast(func.sum(Attendance.tickets), Float)/Event.capacity).label("attendance_ratio"))\
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
    return db.query(Attendance.hour, func.sum(Attendance.tickets).label("attendances"))\
             .filter(Attendance.reservation_id == Reservation.id)\
             .filter(Reservation.event_id == event_id)\
             .group_by(Attendance.hour)\
             .order_by(Attendance.hour)\
             .all()

def all_attendance_per_month(query: QueryDistributionSchema, db: Session):
    q = db.query(func.strftime("%Y-%m", Attendance.date).label("year_month"), func.sum(Attendance.tickets).label("attendances"))\
          .filter(Attendance.reservation_id == Reservation.id)\
          .group_by(func.strftime("%Y-%m", Attendance.date).label("year_month"))\
          .order_by(func.strftime("%Y-%m", Attendance.date).label("year_month"))
    
    if query.init_date:
        q = q.filter(Event.init_date >= query.init_date)
        
    if query.end_date:
        q = q.filter(Event.init_date <= query.end_date)
    
    return q.all()

def all_event_per_month(query: QueryDistributionSchema, db: Session):
    q = db.query(func.strftime("%Y-%m", Event.create_date).label("year_month"), func.sum(Event.id).label("events"))\
          .group_by(func.strftime("%Y-%m", Event.create_date).label("year_month"))\
          .order_by(func.strftime("%Y-%m", Event.create_date).label("year_month"))

    if query.init_date:
        q = q.filter(Event.create_date >= query.init_date)
        
    if query.end_date:
        q = q.filter(Event.create_date <= query.end_date)
        
    return q.all()

def amount_event_per_state(query: QueryDistributionSchema, db: Session):
    q = db.query(Event.state, func.sum(Event.id).label("amount"))\
          .group_by(Event.state)\

    if query.init_date:
        q = q.filter(Event.create_date >= query.init_date)
        
    if query.end_date:
        q = q.filter(Event.create_date <= query.end_date)
        
    return q.all()
