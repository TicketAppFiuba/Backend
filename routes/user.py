from fastapi import APIRouter, Depends
from models.user import User
from controllers import access

router = APIRouter(tags=["Users"])

@router.get("/protected", status_code=200)
async def protected_route(user_db: User = Depends(access.verify)):
    return {"message": f'Hi {user_db.username}, this is a protected route'}