from fastapi import APIRouter
from .user import user_router

v1_router = APIRouter()
v1_router.include_router(user_router, prefix='/users')


@v1_router.get('/')
def hello_v1():
    return {"Hello": "V1"}
