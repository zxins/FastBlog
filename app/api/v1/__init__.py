from fastapi import APIRouter
from .user_api import user_router
from .book_api import book_router

v1_router = APIRouter()
v1_router.include_router(user_router, prefix='/users')
v1_router.include_router(book_router, prefix='/books')


@v1_router.get('/')
def hello_v1():
    return {"Hello": "V1"}
