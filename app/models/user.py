from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import Session
from werkzeug.security import generate_password_hash, check_password_hash

from app.database import Base
from app.utils import file


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, nullable=False)
    username = Column(String(255), unique=True, nullable=False, index=True, default="", comment="用户名")
    nickname = Column(String(255), nullable=False, default="", comment="昵称")
    password = Column(String(255), default="", comment="密码")
    avatar = Column(String(255), default="", comment="头像")
    create_time = Column(DateTime, default=datetime.now, nullable=False, index=True, comment="创建时间")
    update_time = Column(DateTime, default=datetime.now, nullable=False, index=True, comment="更新时间")

    def __str__(self):
        return '<User %s>' % self.nickname

    @staticmethod
    def add(db: Session, username: str, password: str):
        user = db.query(User).filter(User.username == username).first()
        if user is not None:
            return user

        user = User()
        user.username = username
        user.nickname = username
        user.password = generate_password_hash(password)
        user.avatar = file.new_avatar()
        db.add(user)
        db.commit()
        db.refresh(user)
        return user

    @staticmethod
    def get(db: Session, id: int):
        return db.query(User).filter(id=id).first()

    @staticmethod
    def get_by_name(db: Session, username: str):
        return db.query(User).filter(username=username).first()

    @staticmethod
    def page(db: Session, page: int, per_page: int):
        return db.query(User).paginate(page, per_page=per_page)

    def setting(self, nickname: str):
        self.nickname = nickname

    def change_password(self, password: str):
        self.password = generate_password_hash(password)

    def verify_password(self, password: str):
        return check_password_hash(self.password, password)
