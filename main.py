from fastapi import FastAPI

from src.routes import organizer_event, user_access, organizer_access, images, user_event, faqs
from starlette.middleware.sessions import SessionMiddleware
import uvicorn
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(title = "TicketAPP")

origins = ["*"]

app.add_middleware(SessionMiddleware, secret_key="!secret")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_access.router)
app.include_router(organizer_access.router)
app.include_router(organizer_event.router)
app.include_router(user_event.router)
app.include_router(images.router)
app.include_router(faqs.router)


if __name__ == '__main__':
    uvicorn.run('main:app', port=8000, reload=True)
