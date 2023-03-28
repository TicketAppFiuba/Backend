from fastapi import FastAPI
from routes import access, user
from starlette.middleware.sessions import SessionMiddleware
import uvicorn

app = FastAPI(title = "TicketAPP")
app.include_router(access.router)
app.include_router(user.router)
app.add_middleware(SessionMiddleware, secret_key="!secret")

if __name__ == '__main__':
    uvicorn.run('main:app', port=8000, reload=True)