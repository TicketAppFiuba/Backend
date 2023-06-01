from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.config.db import get_db
from src.schemas.complaint import *
from src.config.complaint import *
from src.config import statistics
from src.controllers.admin.access import verify
from src.schemas.statistics import QueryDistributionSchema
from typing import Optional

adm = APIRouter(tags=["Admin | Statistics"])

@adm.get("/admin/complaints/users/ranking", status_code=200)
def user_ranking(admin: str = Depends(verify), db: Session = Depends(get_db)):
    return getRankingFromUsers(db)

@adm.get("/admin/complaints/events/ranking", status_code=200)
def event_ranking(admin: str = Depends(verify), db: Session = Depends(get_db)):
    return getRankingFromEvents(db)

@adm.get("/admin/attendances/statistics/distribution", status_code=200)
def attendances_distribution(query: QueryDistributionSchema, admin: str = Depends(verify), db: Session = Depends(get_db)):
    return statistics.all_attendance_per_month(query, db)

@adm.get("/admin/events/statistics/distribution", status_code=200)
def events_distribution(query: QueryDistributionSchema, admin: str = Depends(verify), db: Session = Depends(get_db)):
    return statistics.all_event_per_month(query, db)

@adm.get("/admin/event/statistics/state", status_code=200)
def events_state(query: QueryDistributionSchema, admin: str = Depends(verify), db: Session = Depends(get_db)):
    return statistics.amount_event_per_state(query, db)