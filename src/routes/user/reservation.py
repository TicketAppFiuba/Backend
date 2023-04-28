from fastapi import APIRouter, Depends
from src.config.db import get_db
from sqlalchemy.orm import Session
from src.controllers.user.access import verify
from src.models.user import User
from src.controllers.user.reservation import *

user_reservation = APIRouter(tags=["User | Reservations"])

@user_reservation.post("/user/event/reservation", status_code=200)
def reserve(reservationSchema: ReservationCreateSchema, user_db: User = Depends(verify), db: Session = Depends(get_db)):
    return create_reservation(reservationSchema, user_db, db)

@user_reservation.get("/user/reservations", status_code=200)
def reservations(user_db: User = Depends(verify), db: Session = Depends(get_db)):
    return get_reservations_from_user(user_db, db)




