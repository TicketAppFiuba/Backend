from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.config.db import get_db
from src.schemas.complaint import *
from src.config.complaint import *
from src.controllers.admin.access import verify

adm = APIRouter(tags=["Admin | Statistics"])

@adm.get("/admin/complaints/users/ranking", status_code=200)
def user_ranking(admin: str = Depends(verify), db: Session = Depends(get_db)):
    return getRankingFromUsers(db)

@adm.get("/admin/complaints/events/ranking", status_code=200)
def event_ranking(admin: str = Depends(verify), db: Session = Depends(get_db)):
    return getRankingFromEvents(db)
