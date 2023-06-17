from sqlalchemy.orm import Session
from src.schemas.event import EventSchema
from src.models.event import Event
from src.schemas.query import QuerySchema
from src.models.faq import FAQ
from src.config.relations import *
from src.schemas.user import UserSchema
from src.config import authorizer
from sqlalchemy.sql import func
from sqlalchemy import func
from datetime import datetime

def create(event: EventSchema, email: str, db: Session):
    event_db = Event(**event.dict(exclude={'authorizers', 'ubication', 'agenda', 'faqs', 'images'}),
                     vacancies=event.capacity,
                     direction=event.ubication.direction,
                     latitude=event.ubication.latitude,
                     longitude=event.ubication.longitude,
                     create_date=datetime.now().date(), 
                     organizer_email=email)
    
    for auth in event.authorizers:            
        if authorizer.get(auth.email, db) is None:
            authorizer.create(UserSchema(email=auth.email, name=auth.email), db)
    
    if authorizer.get(email, db) is None:
        authorizer.create(UserSchema(email=email, name=email), db)

    addRelationsToEvent(event_db, event, email)        
    db.add(event_db)
    db.commit()
    db.refresh(event_db)
    return event_db

def update(event_db: Event, event: dict(), db: Session):
    updateRelationsToEvent(event_db, event)
    for attr, value in event.items():
        setattr(event_db, attr, value)
    db.commit()
    db.refresh(event_db)

def delete(event_db: Event, db: Session):
    db.delete(event_db)
    db.commit()

def reduce_vacancies(event_db: Event, tickets: int, db: Session):
    event_db.vacancies -= tickets
    db.commit()
    db.refresh(event_db)

def change_pic(event_db: Event, pic_id: int, db: Session):
    event_db.pic_id = pic_id
    db.commit()
    db.refresh(event_db)

def suspend(event_db: Event, db: Session):
    event_db.state = "suspended"
    db.commit()
    db.refresh(event_db)

def enable(event_db: Event, db: Session):
    event_db.state = "published"
    db.commit()
    db.refresh(event_db)

def finish(event_db: Event, db: Session):
    event_db.state = "finished"
    db.commit()
    db.refresh(event_db)

def getAll(querySchema: QuerySchema, offset: int, limit: int, db: Session):
    query = db.query(Event).filter(Event.state == "published")
    if querySchema.title is not None:
        query = query.filter(Event.title.ilike('%{}%'.format(querySchema.title)))
    if querySchema.category is not None:
        query = query.filter(Event.category == querySchema.category)
    if querySchema.ubication is not None:
        query = query.order_by(func.sqrt(
                                func.power(Event.latitude-querySchema.ubication.latitude, 2.0)
                                +
                                func.power(Event.longitude-querySchema.ubication.longitude, 2.0)))
    return query.limit(limit).offset(limit*offset).all()
 

def get(event_id: int, db: Session):
    return db.query(Event).filter(Event.id == event_id).first()

def getAllEventFromOrganizer(email: str, db: Session):
    return db.query(Event).filter(Event.organizer_email == email).all()