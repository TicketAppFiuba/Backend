from jose import jwt, JWTError, ExpiredSignatureError
from fastapi import HTTPException
from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from config.user import get, update

class JWTToken:
    def __init__(self, algorithm, duration):
        self.algorithm = algorithm
        self.secret = "f9c27fc8-8e13-4405-9c3e-c46b3d8b356d"
        self.duration = duration

    def create(self, sub: str):
        access_token = {"sub": sub, "exp": datetime.utcnow() + timedelta(minutes=self.duration)}
        jwt_token = jwt.encode(access_token, self.secret, self.algorithm)
        return {"access_token": jwt_token, "token_type": "bearer"}
    
    def auth(self, token: str, db: Session):
        try:
            sub = jwt.decode(token, self.secret, self.algorithm).get("sub")
        except ExpiredSignatureError:
            self.expired(token, db)
        except JWTError:
            raise HTTPException(status_code=401, detail="JWT Error")
        return sub
    
    def expired(self, token: str, db: Session):
        try:
            sub = jwt.decode(token, self.secret, self.algorithm, options={'verify_exp': False}).get("sub")
            user_db = get(sub, db)
            if user_db is not None:
                update(user_db, {"login": False}, db)
            raise HTTPException(status_code=401, detail="JWT Expired")
        except JWTError:
            raise HTTPException(status_code=401, detail="JWT Error")