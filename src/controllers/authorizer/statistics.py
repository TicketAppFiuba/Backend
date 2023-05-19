from sqlalchemy.orm import Session
from src.config import statistics
from src.models.authorizer import Authorizer
from src.controllers.authorizer import permissions

def get_statistics(event_id: int, authorizer_db: Authorizer, db: Session):
    event_db = permissions.check_authorizer_permission(event_id, authorizer_db, db)
    reservation_rate = statistics.reservation_rate(event_db.id, db)
    distribution = statistics.attendance_per_hour(event_db.id, db)
    return {"Reservation_rate": reservation_rate, "Distribution": distribution}