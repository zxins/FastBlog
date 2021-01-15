from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.user import UserModel
from app.schemas.user import UserRegisterSchema, UserLoginSchema

user_router = APIRouter()


@user_router.post('/register')
async def register(user_info: UserRegisterSchema, db: Session = Depends(get_db)):
    user = UserModel.add(db, user_info.username, user_info.password)
    del user.password
    return user


@user_router.post('/login')
async def login(login_info: UserLoginSchema, db: Session = Depends(get_db)):
    user = UserModel.get_by_name(db, login_info.username)
    isAuth = user.verify_password(login_info.password)
    if isAuth:
        return {'msg': '登录成功'}
    return {'errMsg': '登录失败'}
