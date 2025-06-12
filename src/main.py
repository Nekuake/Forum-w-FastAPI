import os
from fastapi import FastAPI
from configuration import settings
app = FastAPI()

os.makedirs(settings.USER_CONTENT_DIR, exist_ok=True)


Base.metadata.create_all(bind=engine)
