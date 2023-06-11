from sqlalchemy.orm import Session
from src.models.event import Event
from sqlalchemy import func, cast, Float
from src.models.attendance import Attendance
from src.models.user import User
from src.models.suspension import Suspension
from src.models.complaint import Complaint
from src.models.reservation import Reservation
from src.schemas.statistics import QueryDistributionSchema
from sqlalchemy import desc

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

def date_filter(unit: str):
    return {
        "month": "%Y-%m",
        "day": "%Y-%m-%d",
        "year": "%Y"
    }[unit]

def all_attendances_per_date(query: QueryDistributionSchema, db: Session):
    q = db.query(func.strftime(date_filter(query.unit), Attendance.date).label("date"), func.sum(Attendance.tickets).label("attendances"))\
          .filter(Attendance.reservation_id == Reservation.id)\
          .group_by(func.strftime(date_filter(query.unit), Attendance.date).label("date"))\
          .order_by(func.strftime(date_filter(query.unit), Attendance.date).label("date"))
    
    if query.init_date:
        q = q.filter(Attendance.date >= query.init_date)
        
    if query.end_date:
        q = q.filter(Attendance.date <= query.end_date)
    
    return q.all()

def all_complaints_per_date(query: QueryDistributionSchema, db: Session):
    q = db.query(func.strftime(date_filter(query.unit), Complaint.date).label("date"), func.count(Complaint.id).label("complaints"))\
          .group_by(func.strftime(date_filter(query.unit), Complaint.date).label("date"))\
          .order_by(func.strftime(date_filter(query.unit), Complaint.date).label("date"))
    
    if query.init_date:
        q = q.filter(Complaint.date >= query.init_date)
        
    if query.end_date:
        q = q.filter(Complaint.date <= query.end_date)
    
    return q.all()

def all_events_per_date(query: QueryDistributionSchema, db: Session):
    q = db.query(func.strftime(date_filter(query.unit), Event.create_date).label("date"), func.count(Event.id).label("events"))\
          .group_by(func.strftime(date_filter(query.unit), Event.create_date).label("date"))\
          .order_by(func.strftime(date_filter(query.unit), Event.create_date).label("date"))

    if query.init_date:
        q = q.filter(Event.create_date >= query.init_date)
        
    if query.end_date:
        q = q.filter(Event.create_date <= query.end_date)
        
    return q.all()

def all_suspensions_per_date(query: QueryDistributionSchema, db: Session):
    q = db.query(func.strftime(date_filter(query.unit), Suspension.date).label("date"), func.count(Suspension.id).label("suspensions"))\
          .group_by(func.strftime(date_filter(query.unit), Suspension.date).label("date"))\
          .order_by(func.strftime(date_filter(query.unit), Suspension.date).label("date"))

    if query.init_date:
        q = q.filter(Suspension.date >= query.init_date)
        
    if query.end_date:
        q = q.filter(Suspension.date <= query.end_date)
        
    return q.all()

def amount_event_per_state(query: QueryDistributionSchema, db: Session):
    q = db.query(Event.state, func.count(Event.id).label("amount"))\
          .group_by(Event.state)\

    if query.init_date:
        q = q.filter(Event.create_date >= query.init_date)
        
    if query.end_date:
        q = q.filter(Event.create_date <= query.end_date)
        
    return q.all()

def top_organizers_by_number_of_events(query: QueryDistributionSchema, db: Session):
    q = db.query(Event.organizer_email, func.count(Event.organizer_email).label("amount"))\
          .group_by(Event.organizer_email)\
          .order_by(desc(func.count(Event.organizer_email).label("amount")))

    if query.category:
        q = q.filter(Event.category == query.category)

    if query.init_date:
        q = q.filter(Event.create_date >= query.init_date)
        
    if query.end_date:
        q = q.filter(Event.create_date <= query.end_date)
    
    return q.all()

def top_organizers_by_attendances(query: QueryDistributionSchema, db: Session):
    q = db.query(Event.organizer_email, func.sum(Attendance.tickets).label("attendances"))\
          .filter(Event.id == Reservation.event_id)\
          .filter(Reservation.id == Attendance.reservation_id)\
          .group_by(Event.organizer_email)
    
    if query.category:
        q = q.filter(Event.category == query.category)

    if query.init_date:
        q = q.filter(Attendance.date >= query.init_date)
        
    if query.end_date:
        q = q.filter(Attendance.date <= query.end_date)
        
    return q.all()

def top_users_by_complaints(db: Session):
    return db.query(User.id, User.email, User.name, User.suspended, func.count(Complaint.id).label("denounce"))\
             .filter(User.id == Complaint.user_id)\
             .group_by(User.id)\
             .order_by(func.count(Complaint.id).desc())\
             .limit(10)\
             .all()

def top_events_by_complaints(db: Session):
    return db.query(Event.id, Event.title, func.count(Complaint.id).label("denounce"))\
             .filter(Complaint.event_id == Event.id)\
             .group_by(Event.id)\
             .order_by(func.count(Complaint.id).desc())\
             .limit(10)\
             .all()