from sqlalchemy.orm import Session
from src.config import event, image, faq
from src.schemas.image import *
from src.schemas.query import QuerySchema
from src.controllers.user.validations import *

def get_event(event_id: int, db: Session):
    event_db = validate_event(event_id, db)
    images_db = image.getAllFromEvent(event_id, db)
    faq_db = faq.getAllFromEvent(event_id, db)
    return {"Event": event_db, "Images": images_db, "FAQ": faq_db}

def update_vacancies(event_id: int, tickets: int, db: Session):
    event_db = validate_event(event_id, db)
    event.update(event_db, {"vacancies": event_db.vacancies-tickets}, db)

def get_all_event(query: QuerySchema, offset: int, limit: int, db: Session):
    events_db = event.getAll(query, offset, limit, db) 
    event_list = []
    for i in events_db:
        event_list.append(get_event(i.id, db))
    return event_list