from fastapi import APIRouter

v1_router = APIRouter()


@v1_router.get('/')
def hello_v1():
    return {"Hello": "V1"}
