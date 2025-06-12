
import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    SECRET_KEY = os.environ.get("SECRET_KEY")
    DATABASE_URL = os.environ.get("DATABASE_URL")
    USER_CONTENT_DIR = os.environ.get("USER_CONTENT_DIR")

settings = Settings()