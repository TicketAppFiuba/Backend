from fastapi import APIRouter, Depends
from src.config.db import get_db
from sqlalchemy.orm import Session
from src.controllers.authorizer.access import verify
from src.controllers.authorizer import authorizer
from src.models.authorizer import Authorizer
from src.schemas.qr import *

router = APIRouter(tags=["QR | Authorizer"])

@router.post("/authorizer/ticket", status_code=200)
def authorize(qr: QRSchema, authorizer_db: Authorizer = Depends(verify), db: Session = Depends(get_db)):
    return authorizer.authorize(qr, authorizer_db, db)