from src.schemas.reservation import *
from src.models.user import User
from sqlalchemy.orm import Session
from src.config import reservation
from src.controllers.user import permissions
from src.controllers.user import event

def create_reservation(reservationSchema: ReservationCreateSchema, user_db: User, db: Session):
    reservationSchema = permissions.check_create_reservation(reservationSchema, user_db, db)
    event.update_vacancies(reservationSchema.event_id, reservationSchema.tickets, db)
    reservation_db = reservation.create(reservationSchema, db)
    return {"detail": "Reservation created successfully", "code": reservation_db.code}

def get_reservations_from_user(user_db: User, db: Session):
    return reservation.getAllFromUser(user_db.id, db)
