from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.config import config
from app.plugin import app_sqlalchemy

engine = create_engine(
    config.SQLALCHEMY_DATABASE_URI
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, query_cls=app_sqlalchemy.BaseQuery)

Base = declarative_base()


def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
