from src.models.authorizer import Authorizer
from sqlalchemy.orm import Session
from src.schemas.user import UserSchema
from src.models.event_authorizer import EventAuthorizer
from src.models.event import Event
from src.models.image import Image

def create(user: UserSchema, db: Session):
    user_db = Authorizer(email=user.email, name=user.name, login=True)
    db.add(user_db)
    db.commit()
    db.refresh(user_db)
    return user_db

def update(user_db: Authorizer, new_attributes: dict(), db: Session):
    for attr, value in new_attributes.items():
        setattr(user_db, attr, value)
    db.commit()
    db.refresh(user_db)
    return user_db

def get(email: str, db: Session):
    return db.query(Authorizer).filter(Authorizer.email == email).first()

def getAllEvents(auth_email: str, db: Session):
    return db.query(Event, Image.link).filter(EventAuthorizer.email == auth_email).filter(EventAuthorizer.event_id == Event.id).filter(Event.pic_id == Image.id).all()

def canScan(auth_email: str, event_id: int, db: Session):
    return db.query(EventAuthorizer).filter(EventAuthorizer.event_id == event_id).filter(EventAuthorizer.email == auth_email).first() is not None

def getAllFromEvent(event_id: int, db: Session):
    return db.query(EventAuthorizer).filter(EventAuthorizer.event_id == event_id).all()