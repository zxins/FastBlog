from datetime import datetime

from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Boolean
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.orm import relationship, deferred

from app.database import Base
from app.models.user import User


class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True, nullable=False, comment="主键id")
    name = Column(String(255), default="", nullable=False, index=True, comment="书名")
    access = Column(Integer, default=1, nullable=False, index=True, comment="允许访问")
    status = Column(Integer, default=0, nullable=False, index=True, comment="状态")  # publish status
    brief = deferred(Column(Text, default="", nullable=False, comment="摘要"))
    select_catalog = Column(Integer, default=0, nullable=False, comment="选择目录")
    publish_timestamp = Column(DateTime, default=datetime.now, nullable=False, index=True, comment="发布时间")
    cover = Column(String(255), default="", nullable=False, comment="封面")
    create_time = Column(DateTime, default=datetime.now, nullable=False, index=True, comment="创建时间")
    update_time = Column(DateTime, default=datetime.now, nullable=False, index=True, comment="更新时间")

    user_id = Column(Integer, ForeignKey(User.__tablename__ + ".id",
                                         ondelete="CASCADE", onupdate="CASCADE"), nullable=False, comment="关联用户id")
    catalogs = relationship("BookCatalog", backref="book", lazy="dynamic", passive_deletes=True)
    images = relationship("BookImage", backref="book", lazy="select", passive_deletes=True)


class BookCatalog(Base):
    __tablename__ = 'book_catalogs'

    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String(255), default="", nullable=False, index=True)
    markdown = deferred(Column(LONGTEXT, default="", nullable=False))
    html = deferred(Column(LONGTEXT, default="", nullable=False))
    publish_markdown = deferred(Column(LONGTEXT, default='', nullable=False))
    publish_html = deferred(Column(LONGTEXT, default='', nullable=False))
    status = Column(Integer, default=0, nullable=True, index=True)
    abstract = deferred(Column(String(255), default=""))
    publish_order = Column(Integer, default=0, nullable=True, index=True)
    pos = Column(Integer, default=0, nullable=False, index=True)
    parent_id = Column(Integer, default=0, nullable=False, index=True)
    is_dir = Column(Boolean, default=False, nullable=False, index=True)
    publish_timestamp = Column(DateTime, default=datetime.now, nullable=False, index=True)
    first_publish = Column(DateTime, default=datetime.now, nullable=False, index=True)
    create_time = Column(DateTime, default=datetime.now, nullable=False, index=True, comment="创建时间")
    update_time = Column(DateTime, default=datetime.now, nullable=False, index=True, comment="更新时间")

    book_id = Column(Integer, ForeignKey(Book.__tablename__ + ".id",
                                         ondelete="CASCADE", onupdate="CASCADE"), nullable=False)


class BookImage(Base):
    __tablename__ = 'book_images'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(255), default="", nullable=False)
    filename = Column(String(255), default="", nullable=False)
    create_time = Column(DateTime, default=datetime.now, nullable=False, index=True, comment="创建时间")

    book_id = Column(Integer, ForeignKey(Book.__tablename__ + ".id",
                                         ondelete="CASCADE", onupdate="CASCADE"), nullable=False)
