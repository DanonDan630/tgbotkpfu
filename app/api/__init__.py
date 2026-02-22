from fastapi import FastAPI
from app.api.routes import router

api_app = FastAPI()
api_app.include_router(router, prefix="/api")