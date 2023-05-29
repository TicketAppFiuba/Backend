from sqlalchemy.orm import Session
from src.models.user import User
from src.config import favorite
from src.controllers.user import permissions

def add_favorite(event_id: int, user_db: User, db: Session):
    permissions.check_add_favorite_event(user_db.id, event_id, db)
    favorite.create(event_id, user_db.id, db)
    return {"detail": "The event was added successfully."}

def delete_favorite(event_id: int, user_db: User, db: Session):
    favorite_db = permissions.check_delete_favorite_event(user_db.id, event_id, db)
    favorite.delete(favorite_db, db)
    return {"detail": "The event was deleted succesfully."}

def get_favorites(user_db: User, db: Session):
    return favorite.getAllFromUser(user_db.id, db)