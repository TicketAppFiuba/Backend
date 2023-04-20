from sqlalchemy.orm import Session
from src.schemas.reservation import ReservationSchema
from src.models.reservation import Reservation
from src.models.event import Event

def create(reservation: ReservationSchema, db: Session):
    reservation_db = Reservation(**reservation.dict())
    db.add(reservation_db)
    db.commit()
    db.refresh(reservation_db)
    return reservation_db

def getByUserAndEvent(user_id: int, event_id: int, db: Session):
    return db.query(Reservation).filter(Reservation.user_id == user_id).filter(Reservation.event_id == event_id).first()

def getAllFromUser(user_id: int, db: Session):
    return db.query(Reservation, Event).filter(Reservation.user_id == user_id).filter(Event.id == Reservation.event_id).all()

def get(reservation_id: int, db: Session):
    return db.query(Reservation).filter(Reservation.id == reservation_id).first()