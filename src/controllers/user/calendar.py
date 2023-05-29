from sqlalchemy.orm import Session
from src.models.user import User
from src.models.event import Event
from src.schemas.event import *
from src.config import image
from src.config import calendar
from src.controllers.user import permissions
from src.config import calendar

def add_calendar(event_id: int, user_db: User, db: Session):
    permissions.check_add_calendar_event(user_db.id, event_id, db)
    calendar.create(event_id, user_db.id, db)
    return {"detail": "The event was added successfully."}

def delete_calendar(event_id: int, user_db: User, db: Session):
    calendar_db = permissions.check_delete_calendar_event(user_db.id, event_id, db)
    calendar.delete(calendar_db, db)
    return {"detail": "The event was deleted succesfully."}

def get_events(user_db: User, db: Session):
    events_list = []
    user_events = calendar.getAllFromUser(user_db.id, db)
    for event in user_events:
        events_list.append(get_event_with_cover_pic(event, db))
    return events_list

def get_event_with_cover_pic(event: Event, db: Session):
    event_with_cover_pic = EventSchemaOutWithLink.from_orm(event)
    cover_image = image.getCoverImage(event.pic_id, db)
    if cover_image is not None:
        event_with_cover_pic.link = cover_image.link
    return event_with_cover_pic