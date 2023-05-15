from sqlalchemy.orm import Session
from src.schemas.complaint import *
from src.models.complaint import Complaint
from src.models.user import User
from src.models.event import Event
from sqlalchemy import func
from datetime import date

def create(complaint: ComplaintSchema, db: Session):
    complaint_db = Complaint(**complaint.dict(), date=date.today())
    db.add(complaint_db)
    db.commit()
    db.refresh(complaint_db)
    return complaint_db

def getAll(query: ComplaintQuerySchema,db: Session):
    complaints = db.query(Complaint, User, Event).join(User, Event)
    if query.category is not None:
        complaints = complaints.filter(Complaint.category == query.category)
    if (query.date_init is not None) and (query.date_end is not None):
        complaints = complaints.filter(query.date_init <= Complaint.date).filter(Complaint.date <= query.date_end)
    return complaints.all()

def getAllFromUser(user_id: int, db: Session):
    return db.query(Complaint, Event.title).join(Event).filter(Complaint.user_id == user_id).all()

def getAllFromEvent(event_id: int, db: Session):
    return db.query(Complaint).filter(Complaint.event_id == event_id).all()

def getByUserAndEvent(user_id: int, event_id: int, db: Session):
    return db.query(Complaint).filter(Complaint.user_id == user_id).filter(Complaint.event_id == event_id).first()

def getAllCategorys(db: Session):
    return db.query(Complaint.category).distinct().all()

def getRankingFromUsers(db: Session):
    return db.query(User.id, User.email, User.name, User.suspended, func.count(Complaint.id).label("denounce"))\
             .filter(User.id == Complaint.user_id)\
             .group_by(User.id)\
             .order_by(func.count(Complaint.id).desc())\
             .limit(10)\
             .all()

def getRankingFromEvents(db: Session):
    return db.query(Event.id, Event.title, func.count(Complaint.id).label("denounce"))\
             .filter(Complaint.event_id == Event.id)\
             .group_by(Event.id)\
             .order_by(func.count(Complaint.id).desc())\
             .limit(10)\
             .all()
