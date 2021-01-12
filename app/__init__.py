from fastapi import FastAPI
from app.config import config
from app.api.v1 import v1_router
from app.admin import admin_router

def create_app():
    app = FastAPI(
        title="Fast Blog",
        version="0.1.1",
        docs_url=config.DOCS_URL,
        openapi_url=config.OPENAPI_URL,
        redoc_url=config.REDOC_URL,
    )

    app.include_router(v1_router, prefix="/api/v1")
    app.include_router(admin_router, prefix='/admin')

    return app
