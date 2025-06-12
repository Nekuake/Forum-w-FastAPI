from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.sql import func
from src.database import Base


class BaseInternals(Base):
    __tablename__ = 'base_internals'
    id = Column(Integer, primary_key=True, autoincrement=True)

class Admin(BaseInternals):
    __tablename__ = 'admin'