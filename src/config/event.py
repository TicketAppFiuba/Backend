from sqlalchemy.orm import Session
from src.schemas.event import EventSchema
from src.models.event import Event
from src.models.image import Image

def create(event: EventSchema, email: str, db: Session):
    event_db = Event(**event.dict(exclude={'images'}), organizer_email=email)
    for img in event.images:
        event_db.images.append(Image(link=img.link, event_id=event_db.id))
    db.add(event_db)
    db.commit()
    db.refresh(event_db)
    return event_db