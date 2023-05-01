from sqlalchemy.orm import Session
from src.schemas.reservation import ReservationSchema
from src.models.reservation import Reservation
from src.models.event import Event
import uuid

def create(reservation: ReservationSchema, db: Session):
    reservation_db = Reservation(**reservation.dict(), code=str(uuid.uuid4()), scanned=False)
    db.add(reservation_db)
    db.commit()
    db.refresh(reservation_db)
    return reservation_db

def scan(reservation_db: Reservation, db: Session):
    reservation_db.scanned = True
    db.commit()
    db.refresh(reservation_db)

def getByUserAndEvent(user_id: int, event_id: int, db: Session):
    return db.query(Reservation).filter(Reservation.user_id == user_id).filter(Reservation.event_id == event_id).first()

def getAllFromUser(user_id: int, db: Session):
    return db.query(Reservation, Event).filter(Reservation.user_id == user_id).filter(Event.id == Reservation.event_id).all()

def get(reservation_code: str, db: Session):
    return db.query(Reservation).filter(Reservation.code == reservation_code).first()