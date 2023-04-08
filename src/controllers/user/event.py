from fastapi import HTTPException
from sqlalchemy.orm import Session
from src.config import event
from src.schemas.image import *
from src.schemas.query import QuerySchema

def get_event(event_id: int, db: Session):
    return event.get(event_id, db)

def get_all_event(query: QuerySchema, offset: int, limit: int, db: Session):
    return event.getAll(query, offset, limit, db) 