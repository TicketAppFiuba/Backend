from sqlalchemy.orm import Session
from src.schemas.event import EventSchema
from src.models.event import Event
from src.schemas.query import QuerySchema

def create(event: EventSchema, email: str, db: Session):
    event_db = Event(**event.dict(exclude={'ubication'}),
                     direction=event.ubication.direction,
                     latitude = event.ubication.latitude,
                     length = event.ubication.length, 
                     organizer_email=email)
    db.add(event_db)
    db.commit()
    db.refresh(event_db)
    return event_db

def update(event_db: Event, event: dict(), db: Session):
    for attr, value in event.items():
        setattr(event_db, attr, value)
    db.commit()
    db.refresh(event_db)

def delete(event_db: Event, db: Session):
    db.delete(event_db)
    db.commit()

def get(event_id: int, db: Session):
    return db.query(Event).filter(Event.id == event_id).first()

def getAllEventFromOrganizer(email: str, db: Session):
    return db.query(Event).filter(Event.organizer_email == email).all()

def getAll(querySchema: QuerySchema, offset: int, limit: int, db: Session):
    query = db.query(Event)
    if querySchema.title is not None:
        query = query.filter(Event.title == querySchema.title)
    if querySchema.category is not None:
        query = query.filter(Event.category == querySchema.category)
    return query.limit(limit).offset(limit*offset).all()
