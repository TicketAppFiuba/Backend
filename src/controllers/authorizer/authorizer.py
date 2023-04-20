from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from src.models.authorizer import Authorizer
from src.config import reservation
from src.config import authorizer
from src.schemas.qr import *

def authorize(qr: QRSchema, authorizer_db: Authorizer, db: Session):
    reservation_db = reservation.get(qr.reservation_id, db)
    if reservation_db is None:
        raise HTTPException(status_code=404, detail="Reservation not exist.")
    if authorizer.canScan(authorizer_db.email, reservation_db.event_id, db) is False:
        raise HTTPException(status_code=403, detail="Not permission.")
    return {"detail": "The authorizer has permission for scan."} 

def get_events(authorizer_db: Authorizer, db: Session):
    return authorizer.getAllEvents(authorizer_db.email, db)