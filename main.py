import uvicorn
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware
from fastapi.middleware.cors import CORSMiddleware
from src.routes.authorizer.access import authorizer_access
from src.routes.authorizer.authorizer import authorizer_authorize
from src.routes.organizer.access import organizer_access
from src.routes.organizer.event import organizer_event
from src.routes.organizer.faq import organizer_faq
from src.routes.organizer.images import organizer_images
from src.routes.user.access import user_access
from src.routes.user.event import user_event
from src.routes.user.reservation import user_reservation
from src.routes.user.complaints import user_complaints
from src.routes.user.firebase import firebase
from src.routes.admin.statistics import adm
from src.routes.admin.moderation import adm_moderation
from src.routes.admin.access import adm_access
from src.routes.admin.event import adm_event
from src.routes.admin.complaints import adm_complaint
from src.services.firebase import initialize_firebase
from src.routes.user.favorites import user_favorites
from src.routes.user.calendar import user_calendar
from src.routes.authorizer.attendances import authorizer_attendances
from src.routes.authorizer.statistics import authorizer_statistics
from threading import Thread, Event
from notification_process import reminder_notifications
from date_process import change_status_to_finalished

app = FastAPI(title = "TicketAPP")

app.add_event_handler("startup", initialize_firebase)

origins1 = ["http://localhost",
           "https://localhost", 
           "http://localhost:8080",
           "http://localhost:8000",
           "http://localhost:3000",
           "http://localhost:5000",
           "https://backend-ticketapp.onrender.com",
           "https://google.com",
           "https://mail.google.com",
           "https://accounts.google.com",
           "https://web-organizacion.vercel.app",
           "https://web-organization-ticketappfiuba.vercel.app",
           "https://back-office-investor.vercel.app",
           "https://back-office-investor-ticketappfiuba.vercel.app",
           "http://localhost:19006"]
           
origins2 = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins2,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(organizer_access)
app.include_router(organizer_event)
app.include_router(organizer_images)
app.include_router(organizer_faq)
app.include_router(user_access)
app.include_router(user_event)
app.include_router(user_reservation)
app.include_router(user_complaints)
app.include_router(user_favorites)
app.include_router(user_calendar)
app.include_router(authorizer_access)
app.include_router(authorizer_authorize)
app.include_router(adm)
app.include_router(adm_moderation)
app.include_router(adm_access)
app.include_router(adm_event)
app.include_router(adm_complaint)
app.include_router(authorizer_attendances)
app.include_router(authorizer_statistics)
app.include_router(firebase)
app.add_middleware(SessionMiddleware, secret_key="!secret")

stop_flag = Event()

@app.on_event("shutdown")
async def shutdown_event():
    stop_flag.set()
    print("Stopping notifications thread.")

if __name__ == '__main__':
    initialize_firebase()
    notifications_thread = Thread(target=reminder_notifications, args=(stop_flag,), daemon=True)
    notifications_thread.start()
    control_event_thread = Thread(target=change_status_to_finalished, args=(stop_flag,), daemon=True)
    control_event_thread.start()
    uvicorn.run('main:app', port=8000, reload=True)
