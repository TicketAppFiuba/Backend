from src.schemas.reservation import *
from src.models.user import User
from sqlalchemy.orm import Session
from src.config import reservation
from src.controllers.user import permissions
from src.controllers.user import event
from src.config import image, notifications, favorite
from src.schemas.event import *
from src.schemas.reservation import *
from src.models.event import Event

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
        reservation_list.append(get_reservation(res, user_db, db))
    return reservation_list

def get_reservation(res, user: User, db: Session):
    reservation_schema = ReservationOutSchema.from_orm(res[1])
    cover_image = image.getCoverImage(res[1].pic_id, db)
    if cover_image is not None:
        reservation_schema.link = cover_image.link
    reservation_schema.favorite = (favorite.getByUserAndEvent(user.id, res[1].id, db) != None)
    reservation_schema.code = res[0].code
    return reservation_schema