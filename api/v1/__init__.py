from fastapi import APIRouter
from api.v1.example import exampleApi

api_v1 = APIRouter()

api_v1.include_router(exampleApi.router, tags=['示例api'])
