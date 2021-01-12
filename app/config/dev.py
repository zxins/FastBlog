import os
from typing import Union, Optional

from pydantic import BaseSettings, AnyHttpUrl, IPvAnyAddress


class Config(BaseSettings):
    DOCS_URL: str = "/docs"
    OPENAPI_URL: str = "/openapi.json"
    REDOC_URL: Optional[str] = "/redoc"

    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8
    SECRET_KEY: str = 'aeq)s(*&dWEQasd8**&^9asda_asdasd*&*&^+_sda'

    # MySQL
    MYSQL_USER: str = "root"
    MYSQL_PASS: str = os.environ['MYSQL_PASS']
    MYSQL_HOST: Union[AnyHttpUrl, IPvAnyAddress] = "127.0.0.1"
    MYSQL_DATABASE: str = "fast_blog"

    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASS}@{MYSQL_HOST}/{MYSQL_DATABASE}?charset=utf8mb4"


config = Config()
