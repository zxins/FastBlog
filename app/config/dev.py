import os
from typing import Union, Optional

from pydantic import BaseSettings, AnyHttpUrl, IPvAnyAddress


class Config(BaseSettings):
    # 文档
    DOCS_URL: str = "/docs"
    OPENAPI_URL: str = "/openapi.json"
    REDOC_URL: Optional[str] = "/redoc"

    # token
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8
    SECRET_KEY: str = 'aeq)s(*&dWEQasd8**&^9asda_asdasd*&*&^+_sda'

    # MySQL
    MYSQL_USER: str = "root"
    MYSQL_PASS: str = os.environ['MYSQL_PASS']
    MYSQL_HOST: Union[AnyHttpUrl, IPvAnyAddress] = "127.0.0.1"
    MYSQL_DATABASE: str = "fast_blog"

    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASS}@{MYSQL_HOST}/{MYSQL_DATABASE}?charset=utf8mb4"

    # app目录 - 当前文件所在上级目录
    APP_BASE_DIR = os.path.dirname(os.path.dirname(__file__))
    # 项目目录 - 当前app所在上级目录
    PROJECT_BASE_DIR = os.path.dirname(APP_BASE_DIR)
    # 静态文件
    STATIC_FOLDER = os.path.join(APP_BASE_DIR, 'static')
    # 头像路径
    AVATAR_PATH = "resource/image/avatar"
    # 临时文件路径
    TMP_PATH = "resource/tmp"
    # 图片路径
    IMAGE_PATH = "resource/image/image"
    # 封面路径
    BOOK_COVER_PATH = "resource/image/cover"


config = Config()
