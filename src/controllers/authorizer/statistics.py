from sqlalchemy.orm import Session
from src.config import statistics
from src.models.authorizer import Authorizer
from src.controllers.authorizer import permissions

def get_statistics(event_id: int, authorizer_db: Authorizer, db: Session):
    event_db = permissions.check_authorizer_permission(event_id, authorizer_db, db)
    reservation_date = statistics.reservation_date(event_db.id, db)
    attendance_date = statistics.attendance_date(event_db.id, db)
    distribution_per_hour = statistics.attendance_per_hour(event_db.id, db)
    return { 
            "reservation_date": reservation_date, 
            "attendance_date": attendance_date,
            "distribution_per_hour": distribution_per_hour
            }