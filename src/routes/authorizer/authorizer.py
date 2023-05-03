from fastapi import APIRouter, Depends
from src.config.db import get_db
from sqlalchemy.orm import Session
from src.controllers.authorizer.access import verify
from src.controllers.authorizer import authorizer
from src.models.authorizer import Authorizer
from src.schemas.qr import *
from src.schemas.authorizer import EventOutSchema
from typing import List

authorizer_authorize = APIRouter(tags=["Authorizer | QR"])

@authorizer_authorize.post("/authorizer/ticket", status_code=200)
def authorize(qr: QRSchema, authorizer_db: Authorizer = Depends(verify), db: Session = Depends(get_db)):
    return authorizer.authorize(qr, authorizer_db, db)

@authorizer_authorize.get("/authorizer/events", response_model=List[EventOutSchema], status_code=200)
def get_events(authorizer_db: Authorizer = Depends(verify), db: Session = Depends(get_db)):
    return authorizer.get_events(authorizer_db, db)