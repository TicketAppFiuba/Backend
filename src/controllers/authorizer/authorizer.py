from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from src.models.authorizer import Authorizer
from src.models.event import Event
from src.config import reservation
from src.config import authorizer
from src.config import image
from src.schemas.qr import *
from src.schemas.authorizer import EventOutSchema

def authorize(qr: QRSchema, authorizer_db: Authorizer, db: Session):
    reservation_db = reservation.get(qr.reservation_code, db)
    if reservation_db is None:
        raise HTTPException(status_code=404, detail="La reserva no existe.")
    if authorizer.canScan(authorizer_db.email, reservation_db.event_id, db) is False:
        raise HTTPException(status_code=403, detail="El autorizador no tiene permisos para escanear.")
    if reservation_db.event_id != qr.event_id:
        raise HTTPException(status_code=403, detail="La reserva no coincide con el evento.")
    if reservation_db.scanned == True:
        raise HTTPException(status_code=403, detail="El codigo ya fue escaneado.")
    reservation.scan(reservation_db, db)
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