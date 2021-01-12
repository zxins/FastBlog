import os
from typing import Union, Optional
from pydantic import AnyHttpUrl, BaseSettings, IPvAnyAddress


class Config(BaseSettings):
    # 文档地址
    DOCS_URL: str = "/api/v1/docs"
    # 文档关联请求数据接口
    OPENAPI_URL: str = "/api/v1/openapi.json"
    # 禁用 redoc 文档
    REDOC_URL: Optional[str] = None

    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24
    SECRET_KEY: str = 'aeq)s(*&dWEQasd8**&^9asda_asdasd*&*&^+_sda'

    # MySQL
    MYSQL_USER: str = 'root'
    MYSQL_PASS: str = "zx3620382"
    MYSQL_HOST: Union[AnyHttpUrl, IPvAnyAddress] = "127.0.0.1"
    MYSQL_DATABASE: str = 'fast_blog'

    # Mysql地址
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://{0}:{1}@{2}/{3}?charset=utf8mb4".format(MYSQL_USER, MYSQL_PASS,
                                                                                       MYSQL_HOST, MYSQL_DATABASE)


config = Config()