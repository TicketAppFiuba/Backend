from fastapi import FastAPI
from src.routes import organizer_event, user_access, organizer_access, images, user_event, faq
from starlette.middleware.sessions import SessionMiddleware
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
#from starlette.middleware.cors import CORSMiddleware


app = FastAPI(title = "TicketAPP")

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
           "https://web-organizacion.vercel.app"]
           
origins2 = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins1,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_access.router)
app.include_router(organizer_access.router)
app.include_router(organizer_event.router)
app.include_router(user_event.router)
app.include_router(images.router)
app.include_router(faq.router)
app.add_middleware(SessionMiddleware, secret_key="!secret")


if __name__ == '__main__':
    uvicorn.run('main:app', port=8000, reload=True)
