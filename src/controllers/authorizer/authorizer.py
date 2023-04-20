from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from src.controllers.authorizer import authorizer
from src.controllers.user import reservation
from src.models.authorizer import Authorizer
from src.schemas.qr import *

def authorize(qr: QRSchema, authorizer_db: Authorizer, db: Session):
    # me tengo que fijar que
    # - exista la reserva
    # - que el autorizador tenga permiso para testear el qr
    return 1
