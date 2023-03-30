from fastapi import APIRouter, Depends, HTTPException
from src.config.db import get_db, engine
from sqlalchemy.orm import Session
from src.models import organizer
from src.models.organizer import Organizer
from starlette.requests import Request
from authlib.integrations.starlette_client import OAuthError
from src.controllers import user_access, organizer_access
from src.schemas.user import UserSchema

oauth = user_access.generate_oauth()
router = APIRouter(tags=["Organizer Authentication"])
organizer.Base.metadata.create_all(bind=engine)

@router.get("/organizer/login", status_code=200)
async def login(request: Request):
    redirect_uri = request.url_for('org_auth')
    return await oauth.google.authorize_redirect(request, redirect_uri)

@router.get("/organizer/auth", status_code=200)
async def org_auth(request: Request, db: Session = Depends(get_db)):
    try:
        data = await oauth.google.authorize_access_token(request)
    except OAuthError:
        raise HTTPException(status_code=401, detail="Auth Error.")
    userinfo = data.get('userinfo')
    user = UserSchema(email=userinfo.email, name=userinfo.name)
    return organizer_access.login(user, db)

@router.get("/organizer/logout", status_code=200)
async def logout(request: Request, user_db: Organizer = Depends(organizer_access.verify), db: Session = Depends(get_db)):
    for key in list(request.session.keys()):
        request.session.pop(key)
    return organizer_access.logout(user_db, db)