from jose import jwt, JWTError, ExpiredSignatureError
from fastapi import HTTPException
from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from config.user import get, update
import uuid

class JWTToken:
    def __init__(self, algorithm, duration):
        self.algorithm = algorithm
        self.secret = str(uuid.uuid4())
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
            raise HTTPException(status_code=400, detail="JWT Error")
        return sub
    
    def expired(self, token: str, db: Session):
        try:
            sub = jwt.decode(token, self.secret, self.algorithm, options={'verify_exp': False}).get("sub")
            user_db = get(sub, db)
            if user_db is not None:
                update(user_db, {"login": False}, db)
            raise HTTPException(status_code=400, detail="JWT Expired")
        except JWTError:
            raise HTTPException(status_code=400, detail="JWT Error")