from fastapi import HTTPException
from sqlalchemy.orm import Session
from src.models.authorizer import Authorizer
from src.config import authorizer
from src.schemas.qr import *
from src.controllers.validator import validator
import datetime

def check_authorizer_permission(event_id: int, authorizer_db: Authorizer, db: Session):
    event_db = validator.validate_event(event_id, db)
    if authorizer.canScan(authorizer_db.email, event_id, db) is False:
        raise HTTPException(status_code=403, detail="El autorizador no tiene permisos para escanear.")
    return event_db    

def check_scan_reservation(qr: QRSchema, authorizer_db: Authorizer, db: Session):
    reservation_db = validator.validate_reservation(qr.reservation_code, db)
    event_db = check_authorizer_permission(qr.event_id, authorizer_db, db)
    if reservation_db.event_id != qr.event_id:
        raise HTTPException(status_code=403, detail="La reserva no coincide con el evento.")
    if reservation_db.scanned == True:
        raise HTTPException(status_code=403, detail="El codigo ya fue escaneado.")
    if datetime.datetime.now() < event_db.end_date:
        raise HTTPException(status_code=403, detail="El proceso de autorizacion todavia no ha comenzado.")
    return reservation_db

