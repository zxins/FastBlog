from pydantic import BaseModel


class UserRegisterSchema(BaseModel):
    username: str
    password: str


class UserLoginSchema(BaseModel):
    username: str
    password: str
