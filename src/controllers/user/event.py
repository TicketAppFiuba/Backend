from fastapi import HTTPException
from sqlalchemy.orm import Session
from src.config import event, image, faq
from src.schemas.image import *
from src.schemas.query import QuerySchema

def get_event(event_id: int, db: Session):
    event_db = event.get(event_id, db)
    if event_db is None:
        raise HTTPException(status_code=404, detail="Event not exist.")
    images_db = image.getAllFromEvent(event_id, db)
    faq_db = faq.getAllFromEvent(event_id, db)
    return {"Event": event_db, "Images": images_db, "FAQ": faq_db}

def get_all_event(query: QuerySchema, offset: int, limit: int, db: Session):
    events_db = event.getAll(query, offset, limit, db) 
    event_list = []
    for i in events_db:
        event_list.append(get_event(i.id, db))
    return event_list