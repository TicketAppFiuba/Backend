from fastapi import HTTPException
from sqlalchemy.orm import Session
from src.models.authorizer import Authorizer
from src.config import authorizer
from src.schemas.qr import *
from src.controllers.validator import validator

def check_scan_reservation(qr: QRSchema, authorizer_db: Authorizer, db: Session):
    reservation_db = validator.validate_reservation(qr.reservation_code, db)
    if authorizer.canScan(authorizer_db.email, reservation_db.event_id, db) is False:
        raise HTTPException(status_code=403, detail="El autorizador no tiene permisos para escanear.")
    if reservation_db.event_id != qr.event_id:
        raise HTTPException(status_code=403, detail="La reserva no coincide con el evento.")
    if reservation_db.scanned == True:
        raise HTTPException(status_code=403, detail="El codigo ya fue escaneado.")
    return reservation_db

