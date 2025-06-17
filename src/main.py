import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.database import Base, engine
from src.forum.router import forum_router, post_router
from configuration import settings
app = FastAPI(
    title="Forum implemented with FastAPI",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(forum_router)
app.include_router(post_router)

os.makedirs(settings.USER_CONTENT_DIR, exist_ok=True)


Base.metadata.create_all(bind=engine)
