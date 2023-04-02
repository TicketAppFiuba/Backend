from fastapi import APIRouter, Depends
from src.config.db import get_db
from sqlalchemy.orm import Session
from src.models import event
from src.controllers.user_access import verify
from src.models.user import User
from src.controllers import event

router = APIRouter(tags=["Events | User"])

@router.get("/events", status_code=200)
def get_events(offset: int = 0, limit: int = 15, user_db: User = Depends(verify), db: Session = Depends(get_db)):
    return event.get_all(offset, limit, db)
# Ver una lista de eventos disponibles. Definir disponibilidad. Que haya cupos? que no haya vencido?
# Por ahora imprimo sin restriccion.