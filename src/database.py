from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from exceptions import DatabaseNotSetException
import os

DATABASE_URL = os.getenv("DATABASE_URL")

if DATABASE_URL is None: raise DatabaseNotSetException()

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()