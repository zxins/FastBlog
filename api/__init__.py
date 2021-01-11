from fastapi import FastAPI
from api.v1 import api_v1


def create_app():
    app = FastAPI(title="fast_blog_api")

    app.include_router(api_v1, prefix='/api/v1')
    return app
