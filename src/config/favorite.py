from sqlalchemy.orm import Session
from src.models.favorites import Favorite

def create_favorite(event_id: int, user_id: int, db: Session):
    favorite_db = Favorite(event_id=event_id, user_id=user_id)
    db.add(favorite_db)
    db.commit()
    db.refresh(favorite_db)
    return favorite_db
    
def getAllFromUser(user_id: int, db: Session):
    return db.query(Favorite).filter(Favorite.user_id == user_id).all()

def getByUserAndEvent(user_id: int, event_id: int, db: Session):
    return db.query(Favorite).filter(Favorite.user_id == user_id).filter(Favorite.event_id == event_id).first()