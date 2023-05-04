from sqlalchemy.orm import Session
from src.config import event, image, faq, section
from src.schemas.image import *
from src.schemas.query import QuerySchema
from src.schemas.ubication import UbicationSchema
from src.schemas.coordinate import CoordinateSchema
from src.controllers.validator import validator
from src.controllers.user import haversine

def get_event(event_id: int, db: Session):
    event_db = validator.validate_event(event_id, db)
    images_db = image.getAllFromEvent(event_id, db)
    faq_db = faq.getAllFromEvent(event_id, db)
    diary_db = section.getAllFromEvent(event_id, db)
    return {"Event": event_db, "Images": images_db, "FAQ": faq_db, "Diary": diary_db}

def get_event_with_distance(event_id: int, ubication: UbicationSchema, db: Session):
    event_db = validator.validate_event(event_id, db)
    images_db = image.getAllFromEvent(event_id, db)
    faq_db = faq.getAllFromEvent(event_id, db)
    diary_db = section.getAllFromEvent(event_id, db)
    distance = haversine.distance(CoordinateSchema(latitude=event_db.latitude, longitude=event_db.longitude), CoordinateSchema(latitude=ubication.latitude, longitude=ubication.longitude))
    return {"Event": event_db, "Images": images_db, "FAQ": faq_db, "Diary": diary_db, "Distance": distance}

def update_vacancies(event_id: int, tickets: int, db: Session):
    event_db = validator.validate_event(event_id, db)
    event.reduce_vacancies(event_db, tickets, db)

def get_all_event(query: QuerySchema, offset: int, limit: int, db: Session):
    events_db = event.getAll(query, offset, limit, db) 
    event_list = []
    for i in events_db:
        event_list.append(get_event_with_distance(i.id, query.ubication, db)) 
    return event_list