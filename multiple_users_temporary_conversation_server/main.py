from fastapi import FastAPI
from fastapi.responses import JSONResponse
from app.api.endpoints import chat
from app.middleware.setup import setup_middleware

app = FastAPI()
setup_middleware(app)

app.include_router(chat.router, prefix="/api/v1", tags=["Chatting"])

@app.get('/')
def home():
    return JSONResponse(
        status_code=200,
        content={
            'message': 'Welcome!'
        }
    )