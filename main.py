from fastapi import FastAPI
from src.routes import user_access, organizer_access
from starlette.middleware.sessions import SessionMiddleware
import uvicorn

app = FastAPI(title = "TicketAPP")
app.include_router(user_access.router)
app.include_router(organizer_access.router)
app.add_middleware(SessionMiddleware, secret_key="!secret")

if __name__ == '__main__':
    uvicorn.run('main:app', port=8000, reload=True)
