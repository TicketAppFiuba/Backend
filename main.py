from fastapi import FastAPI

from src.routes import organizer_event, user_access, organizer_access, images, user_event
from starlette.middleware.sessions import SessionMiddleware
import uvicorn
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(title = "TicketAPP")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_access.router)
app.include_router(organizer_access.router)
app.include_router(organizer_event.router)
app.include_router(user_event.router)
app.include_router(images.router)
app.add_middleware(SessionMiddleware, secret_key="!secret")

if __name__ == '__main__':
    uvicorn.run('main:app', port=8000, reload=True)
