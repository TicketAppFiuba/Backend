from fastapi import APIRouter, Depends, HTTPException
from src.config.db import get_db, engine
from sqlalchemy.orm import Session
from src.controllers.organizer import access
from src.models import organizer
from src.models.organizer import Organizer
from starlette.requests import Request
from authlib.integrations.starlette_client import OAuthError
from src.schemas.user import UserSchema
from google.oauth2 import id_token
from google.auth.transport import requests

oauth = access.generate_oauth()
router = APIRouter(tags=["Authentication | Organizer"])
organizer.Base.metadata.create_all(bind=engine)

@router.get("/organizer/login", status_code=200)
async def login(token: str, db: Session = Depends(get_db)):
    try:
        id_info = id_token.verify_oauth2_token(token, requests.Request(), "651976534821-njeiiul5h073b0s321lvn9pevadj3aeg.apps.googleusercontent.com")
    except ValueError:
        raise HTTPException(status_code=400, detail="JWT Invalid.")
    user = UserSchema(name=id_info["name"], email=id_info["email"])
    return access.login(user, db)

@router.get("/organizer/logout", status_code=200)
async def logout(request: Request, user_db: Organizer = Depends(access.verify), db: Session = Depends(get_db)):
    for key in list(request.session.keys()):
        request.session.pop(key)
    return access.logout(user_db, db)