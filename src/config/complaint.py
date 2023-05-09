from sqlalchemy.orm import Session
from src.schemas.complaint import ComplaintSchema
from src.models.complaint import Complaint
from src.models.user import User
from src.models.event import Event
from sqlalchemy import func

def create(complaint: ComplaintSchema, db: Session):
    complaint_db = Complaint(**complaint.dict())
    db.add(complaint_db)
    db.commit()
    db.refresh(complaint_db)
    return complaint_db

def getAll(db: Session):
    return db.query(Complaint).all()

def getAllFromUser(user_id: int, db: Session):
    return db.query(Complaint).filter(Complaint.user_id == user_id).all()

def getByUserAndEvent(user_id: int, event_id: int, db: Session):
    return db.query(Complaint).filter(Complaint.user_id == user_id).filter(Complaint.event_id == event_id).first()

def getRankingFromUsers(db: Session):
    return db.query(User.id, User.email, func.count(Complaint.id).label("denounce"))\
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