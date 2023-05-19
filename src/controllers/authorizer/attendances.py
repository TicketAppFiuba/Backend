from sqlalchemy.orm import Session
from src.config import attendance
from src.controllers.authorizer import permissions
from src.models.authorizer import Authorizer

def get_attendances(event_id: id, authorizer_db: Authorizer, db: Session):
    event_db = permissions.check_authorizer_permission(event_id, authorizer_db, db)
    return attendance.getFromEvent(event_db.id, db)
