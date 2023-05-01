from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from src.models.authorizer import Authorizer
from src.config import reservation
from src.config import authorizer
from src.schemas.qr import *

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
    return authorizer.getAllEvents(authorizer_db.email, db)