from sqlalchemy.orm import Session
from src.schemas.event import EventSchema
from src.models.event import Event
from src.schemas.query import QuerySchema
from src.models.section import Section
from src.models.faq import FAQ
from src.models.event_authorizer import EventAuthorizer
from sqlalchemy.sql import func
from sqlalchemy import func

def create(event: EventSchema, email: str, db: Session):
    event_db = Event(**event.dict(exclude={'authorizers', 'ubication', 'agenda', 'faqs'}),
                     vacancies=event.capacity,
                     direction=event.ubication.direction,
                     latitude = event.ubication.latitude,
                     longitude = event.ubication.longitude, 
                     organizer_email=email)
    for section in event.agenda:
        event_db.sections.append(Section(**section.dict()))

    for faq in event.faqs:
        event_db.faqs.append(FAQ(**faq.dict()))

    event_db.authorizers.append(EventAuthorizer(event_id=event_db.id, email=email))
    for authorizer in event.authorizers:
        event_db.authorizers.append(EventAuthorizer(**authorizer.dict()))
        
    db.add(event_db)
    db.commit()
    db.refresh(event_db)
    return event_db

def update(event_db: Event, event: dict(), db: Session, sections: list = [], faqs: list = []):
    for section in sections:
        event_db.sections.append(Section(**section))

    for faq in faqs:
        event_db.faqs.append(FAQ(**faq))

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
        query = query.filter(Event.title.ilike('%{}%'.format(querySchema.title)))
    if querySchema.category is not None:
        query = query.filter(Event.category == querySchema.category)
    if querySchema.ubication is not None:
        query = query.order_by(func.sqrt(
                                func.power(Event.latitude-querySchema.ubication.latitude, 2.0)
                                +
                                func.power(Event.longitude-querySchema.ubication.longitude, 2.0)))
    return query.limit(limit).offset(limit*offset).all()
 