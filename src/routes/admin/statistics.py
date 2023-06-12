from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.config.db import get_db
from src.schemas.complaint import *
from src.config.complaint import *
from src.config import statistics
from src.controllers.admin.access import verify
from src.schemas.statistics import *
from typing import Optional, Union

adm = APIRouter(tags=["Admin | Statistics"])

@adm.get("/admin/attendances/statistics/distribution", response_model=List[AttendancesDistributionSchema], status_code=200)
def attendances_distribution(                    
                        init_date: Union[date, None] = None,
                        end_date: Union[date, None] = None,
                        unit: Optional[str] = 'month',
                        admin: str = Depends(verify), 
                        db: Session = Depends(get_db)
                    ):
    query = QueryDistributionSchema(init_date=init_date, end_date=end_date, unit=unit)
    return statistics.all_attendances_per_date(query, db)

@adm.get("/admin/events/statistics/distribution", response_model=List[EventsDistributionSchema], status_code=200)
def events_distribution(
                    init_date: Union[date, None] = None,
                    end_date: Union[date, None] = None,
                    unit: Optional[str] = 'month',
                    admin: str = Depends(verify), 
                    db: Session = Depends(get_db)
                ):
    query = QueryDistributionSchema(init_date=init_date, end_date=end_date, unit=unit)
    return statistics.all_events_per_date(query, db)

@adm.get("/admin/complaints/statistics/distribution", response_model=List[ComplaintsDistributionSchema], status_code=200)
def complaints_distribution(
                    init_date: Union[date, None] = None,
                    end_date: Union[date, None] = None,
                    unit: Optional[str] = 'month',
                    admin: str = Depends(verify), 
                    db: Session = Depends(get_db)
                ):
    query = QueryDistributionSchema(init_date=init_date, end_date=end_date, unit=unit)
    return statistics.all_complaints_per_date(query, db)

@adm.get("/admin/suspensions/statistics/distribution", response_model=List[SuspensionsDistributionSchema], status_code=200)
def suspensions_distribution(
                    init_date: Union[date, None] = None,
                    end_date: Union[date, None] = None,
                    unit: Optional[str] = 'month',
                    admin: str = Depends(verify), 
                    db: Session = Depends(get_db)
                ):
    query = QueryDistributionSchema(init_date=init_date, end_date=end_date, unit=unit)
    return statistics.all_suspensions_per_date(query, db)

@adm.get("/admin/event/statistics/state", status_code=200)
def events_state(
                init_date: Union[date, None] = None,
                end_date: Union[date, None] = None, 
                unit: Optional[str] = 'month',
                admin: str = Depends(verify), 
                db: Session = Depends(get_db)
            ):
    query = QueryDistributionSchema(init_date=init_date, end_date=end_date, unit=unit)
    return statistics.amount_event_per_state(query, db)


@adm.get("/admin/events/organizers/ranking", response_model=List[TopOrganizersByNumberOfEventsSchemaOut], status_code=200)
def top_organizer_by_number_of_events(
                init_date: Union[date, None] = None,
                end_date: Union[date, None] = None, 
                unit: Optional[str] = 'month',
                category: Union[str, None] = None,
                admin: str = Depends(verify), 
                db: Session = Depends(get_db)
            ):
    query = QueryDistributionSchema(init_date=init_date, end_date=end_date, category=category, unit=unit)
    return statistics.top_organizers_by_number_of_events(query, db)

@adm.get("/admin/attendances/organizers/ranking", response_model=List[TopOrganizersByAttendancesSchemaOut], status_code=200)
def top_organizer_by_attendances(
                init_date: Union[date, None] = None,
                end_date: Union[date, None] = None,
                unit: Optional[str] = 'month',
                category: Union[str, None] = None,
                admin: str = Depends(verify), 
                db: Session = Depends(get_db)
            ):
    query = QueryDistributionSchema(init_date=init_date, end_date=end_date, category=category, unit=unit)
    return statistics.top_organizers_by_attendances(query, db)

@adm.get("/admin/complaints/users/ranking", status_code=200)
def top_users_by_number_of_complaints(admin: str = Depends(verify), db: Session = Depends(get_db)):
    return statistics.top_users_by_complaints(db)

@adm.get("/admin/complaints/events/ranking", status_code=200)
def top_events_by_number_of_complaints(admin: str = Depends(verify), db: Session = Depends(get_db)):
    return statistics.top_events_by_complaints(db)