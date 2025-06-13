from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.sql import func
from src.database import Base


class BaseEntity(Base):
    __tablename__ = "BaseEntity"
    id = Column(Integer, primary_key=True, autoincrement=True)
    creator_id = Column(Integer, nullable=False)
    created_at = Column(DateTime, nullable=False, server_default=func.now())
    updated_at = Column(DateTime, nullable=False, server_default=func.now(), onupdate=func.now())
    deleted = Column(Boolean, nullable=False, default=False)


class Forum(BaseEntity):
    __tablename__ = 'forum'
    name = Column(String(64), nullable=False)
    description = Column(String(255), nullable=False)

class Post(BaseEntity):
    __tablename__ = 'post'
    name = Column(String(64), nullable=True)
    type = Column(String(64), nullable=False)
    content = Column(String(1024), nullable=False)
    forum_id = Column(ForeignKey(Forum.id), nullable=False)
    parent_post_id = Column(ForeignKey('Post.id'), nullable=True)
