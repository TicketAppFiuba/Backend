from sqlalchemy.orm import Session
from src.models.authorizer import Authorizer
from src.models.event import Event
from src.config import reservation, authorizer, image, attendance
from src.schemas.qr import *
from src.schemas.authorizer import EventOutSchema
from src.controllers.authorizer import permissions

def authorize(qr: QRSchema, authorizer_db: Authorizer, db: Session):
    reservation_db = permissions.check_scan_reservation(qr, authorizer_db, db)
    reservation.scan(reservation_db, db)
    attendance.register(reservation_db.id, reservation_db.tickets, db)
    return {"detail": "La reserva fue escaneada correctamente."} 

def get_events(authorizer_db: Authorizer, db: Session):
    events_list = []
    authorizer_events = authorizer.getAllEvents(authorizer_db.email, db)
    for event in authorizer_events:
        events_list.append(get_event_with_cover_pic(event, db))
    return events_list

def get_event_with_cover_pic(event: Event, db: Session):
    event_with_cover_pic = EventOutSchema.from_orm(event)
    cover_image = image.getCoverImage(event.pic_id, db)
    if cover_image is not None:
        event_with_cover_pic.link = cover_image.link
    return event_with_cover_pic