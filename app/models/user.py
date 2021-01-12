from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship

from app.database import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, nullable=False)
    username = Column(String(255), unique=True, nullable=False, index=True, default="", comment="用户名")
    nickname = Column(String(255), nullable=False, default="", comment="昵称")
    password = Column(String(255), default="", comment="密码")
    avatar = Column(String(255), default="", comment="头像")
    create_time = Column(DateTime, default=datetime.now, nullable=False, index=True, comment="创建时间")
    update_time = Column(DateTime, default=datetime.now, nullable=False, index=True, comment="更新时间")

    books = relationship("Book", backref="user", lazy="dynamic")
