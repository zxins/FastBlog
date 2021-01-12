from fastapi import APIRouter

admin_router = APIRouter()


@admin_router.get('/')
def hello_admin():
    return {"Hello": "Admin"}
