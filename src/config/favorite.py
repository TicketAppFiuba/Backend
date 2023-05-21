from sqlalchemy.orm import Session
from src.models.favorites import Favorite
from src.models.event import Event

def create(event_id: int, user_id: int, db: Session):
    favorite_db = Favorite(event_id=event_id, user_id=user_id)
    db.add(favorite_db)
    db.commit()
    db.refresh(favorite_db)
    return favorite_db

def delete(favorite_db: Favorite, db: Session):
    db.delete(favorite_db)
    db.commit()
    
def getAllFromUser(user_id: int, db: Session):
    return db.query(Event).join(Favorite).filter(Favorite.user_id == user_id).all()

def getByUserAndEvent(user_id: int, event_id: int, db: Session):
    return db.query(Favorite).filter(Favorite.user_id == user_id).filter(Favorite.event_id == event_id).first()