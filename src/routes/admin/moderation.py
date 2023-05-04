from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.config.db import get_db
from src.schemas.complaint import *
from src.config.complaint import *

adm_moderation = APIRouter(tags=["Admin | Moderation"])

@adm_moderation.post("/user/suspend", status_code=200)
def suspend(email: str, db: Session = Depends(get_db)):
    #return suspend_user(user_id, db)
    return 1