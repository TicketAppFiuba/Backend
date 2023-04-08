from fastapi import APIRouter, Depends, HTTPException
from src.config.db import get_db, engine
from sqlalchemy.orm import Session
from src.models import user
from src.models.user import User
from starlette.requests import Request
from authlib.integrations.starlette_client import OAuthError
from src.controllers.user import access
from src.schemas.user import UserSchema

oauth = access.generate_oauth()
router = APIRouter(tags=["Authentication | User"])
user.Base.metadata.create_all(bind=engine)

@router.get("/user/login", status_code=200)
async def login(request: Request):
    redirect_uri = request.url_for('auth')
    return await oauth.google.authorize_redirect(request, redirect_uri)

@router.get("/user/auth", status_code=200)
async def auth(request: Request, db: Session = Depends(get_db)):
    try:
        data = await oauth.google.authorize_access_token(request)
    except OAuthError:
        raise HTTPException(status_code=401, detail="Auth Error.")
    userinfo = data.get('userinfo')
    user = UserSchema(email=userinfo.email, name=userinfo.name)
    return access.login(user, db)

@router.get("/user/logout", status_code=200)
async def logout(request: Request, user_db: User = Depends(access.verify), db: Session = Depends(get_db)):
    for key in list(request.session.keys()):
        request.session.pop(key)
    return access.logout(user_db, db)

