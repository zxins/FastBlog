from sqlalchemy import Column, Integer, String, Boolean
from repository.mysql import Base


class ExampleModel(Base):
    __tablename__ = 'example'

    example_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), unique=True, index=True)
    is_active = Column(Boolean, default=True)


class ItemModel(Base):
    __tablename__ = 'items'

    item_id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(100), nullable=False, default="")
    tags = Column(String(35), nullable=False, default="")