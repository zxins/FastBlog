from datetime import datetime

from passlib.context import CryptContext
from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.orm import Session

from app.database import Base
from app.utils import file

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password):
    return pwd_context.hash(password)


class UserModel(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, nullable=False)
    username = Column(String(255), unique=True, nullable=False, index=True, default="", comment="用户名")
    nickname = Column(String(255), nullable=False, default="", comment="昵称")
    password = Column(String(255), default="", comment="密码")
    avatar = Column(String(255), default="", comment="头像")
    is_active = Column(Boolean, default=True, nullable=False, index=True)
    is_staff = Column(Boolean, default=False, nullable=False, index=True)
    create_time = Column(DateTime, default=datetime.now, nullable=False, index=True, comment="创建时间")
    update_time = Column(DateTime, default=datetime.now, nullable=False, index=True, comment="更新时间")

    def __str__(self):
        return '<UserModel %s>' % self.username

    @staticmethod
    def add(db: Session, username: str, password: str):
        user = db.query(UserModel).filter(UserModel.username == username).first()
        if user is not None:
            return user

        user = UserModel()
        user.username = username
        user.nickname = username
        user.password = get_password_hash(password)
        user.avatar = file.new_avatar()
        db.add(user)
        db.commit()
        db.refresh(user)
        return user

    @staticmethod
    def get(db: Session, id: int):
        return db.query(UserModel).filter(UserModel.id == id).first()

    @staticmethod
    def get_by_name(db: Session, username: str):
        return db.query(UserModel).filter(UserModel.username == username).first()

    @staticmethod
    def page(db: Session, page: int, per_page: int):
        return db.query(UserModel).paginate(page, per_page=per_page)

    def setting(self, nickname: str):
        self.nickname = nickname

    def change_password(self, password: str):
        self.password = get_password_hash(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password)
