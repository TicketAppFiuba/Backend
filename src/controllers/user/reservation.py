from src.schemas.reservation import *
from src.models.user import User
from sqlalchemy.orm import Session
from src.config import reservation
from src.controllers.user import permissions
from src.controllers.user import event
from src.config import image, notifications

def create_reservation(reservationSchema: ReservationCreateSchema, user_db: User, db: Session):
    reservationSchema = permissions.check_create_reservation(reservationSchema, user_db, db)
    event.update_vacancies(reservationSchema.event_id, reservationSchema.tickets, db)
    reservation_db = reservation.create(reservationSchema, db)
    notifications.create_subscription(user_db.id, reservationSchema.event_id, db)
    return {"detail": "Reservation created successfully", "code": reservation_db.code}

def get_reservations_from_user(user_db: User, db: Session):
    reservation_list = []
    reservations = reservation.getAllFromUser(user_db.id, db)
    for res in reservations:
        if res["Event"].pic_id != None:
            res["Event"].pic_id = image.getCoverImage(res["Event"].pic_id, db)
        reservation_list.append(res)
    return reservation_list