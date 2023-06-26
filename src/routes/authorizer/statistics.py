from fastapi import APIRouter, Depends
from src.config.db import get_db
from sqlalchemy.orm import Session
from src.models.authorizer import Authorizer
from src.controllers.authorizer.access import verify
from src.controllers.authorizer import statistics
from src.schemas.statistics import StatisticsSchema

authorizer_statistics = APIRouter(tags=["Authorizer | Statistics"])

@authorizer_statistics.get("/authorizer/event/statistics", status_code=200, response_model=StatisticsSchema)
def event_statistics(event_id: int, authorizer_db: Authorizer = Depends(verify), db: Session = Depends(get_db)):
    return statistics.get_statistics(event_id, authorizer_db, db)

