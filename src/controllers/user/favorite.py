from sqlalchemy.orm import Session
from src.models.user import User
from src.config import favorite
from src.controllers.user import permissions
from src.config import favorite

def add_favorite(event_id: int, user_db: User, db: Session):
    permissions.check_add_favorite_event(user_db.id, event_id, db)
    favorite.create_favorite(event_id, user_db.id, db)
    return {"detail": "The event was added successfully"}

def get_favorites(user_db: User, db: Session):
    return favorite.getAllFromUser(user_db.id, db)