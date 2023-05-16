from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.config.db import get_db
from src.models.user import User
from src.controllers.user.access import verify
from src.controllers.user import favorite

user_favorites = APIRouter(tags=["User | Favorites"])

@user_favorites.post("/user/event/favorite", status_code=200)
def add_favorite(event_id: int, user_db: User = Depends(verify), db: Session = Depends(get_db)):
    return favorite.add_favorite(event_id, user_db, db)
    
@user_favorites.get("/user/favorites", status_code=200)
def get_favorites(user_db: User = Depends(verify), db: Session = Depends(get_db)):
    return favorite.get_favorites(user_db, db)