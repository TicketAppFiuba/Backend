from fastapi import APIRouter
from src.controllers.authorizer import authorizer

router = APIRouter(tags=["QR | Authorizer"])

@router.post("/authorizer/ticket", status_code=200)
def authorize():
    return authorizer.authorize()

# Me llega
    # Id del evento
    # Id de la reserva
    # jwt del patovica
# Devuelvo
    # OK or NOK (?)