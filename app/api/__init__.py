# from datetime import datetime, timedelta
# from typing import Optional
#
# from fastapi import Depends, HTTPException, status
# from fastapi.security import OAuth2PasswordBearer
# from jose import JWTError, jwt
# from sqlalchemy.orm import Session
#
# from app.config import config
# from app.models.user import UserModel
# from app.schemas.user import TokenData
#
# ALGORITHM = "HS256"
#
# oauth2_schema = OAuth2PasswordBearer(tokenUrl="token")
#
#
# def get_user(db: Session, username):
#     user = UserModel.get_by_name(db, username)
#     if not user:
#         return user
#
#
# def authenticate_user(db: Session, username: str, password: str):
#     user = get_user(db, username)
#     if not user:
#         return False
#     if not user.verify_password(password):
#         return False
#     return user
#
#
# def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
#     to_encode = data.copy()
#     if expires_delta:
#         expire = datetime.utcnow() + expires_delta
#     else:
#         expire = datetime.utcnow() + timedelta(minutes=15)
#     to_encode.update({"exp": expire})
#     encode_jwt = jwt.encode(to_encode, config.SECRET_KEY, algorithm=ALGORITHM)
#     return encode_jwt
#
#
# async def get_current_user(db: Session, token: str = Depends(oauth2_schema)):
#     credentials_exception = HTTPException(
#         status_code=status.HTTP_401_UNAUTHORIZED,
#         detail="Could not validate credentials",
#         headers={"WWW-Authenticate": "Bearer"},
#     )
#
#     try:
#         payload = jwt.decode(token, config.SECRET_KEY, algorithms=[ALGORITHM])
#         username: str = payload.get("sub")
#         if username is None:
#             raise credentials_exception
#         token_data = TokenData(username=username)
#     except JWTError:
#         raise credentials_exception
#
#     user = get_user(db, username=token_data.username)  # todo: db_user
#     if user is None:
#         raise credentials_exception
#     return user
#
#
# async def get_current_active_user(current_user: UserModel = Depends(get_current_user)):
#     if not current_user.is_active:
#         raise HTTPException(status_code=400, detail="Inactive user")
#     return current_user
