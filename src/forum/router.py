from http.client import responses

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from src.forum import schemas
from src.forum.service import PostService, ForumService
from src.database import get_db



#Forum
forum_router = APIRouter(
    prefix="/forums",
    tags=["forums"]
)

@forum_router.get("/", response_model=List)
def get_forums(offset:int=0, limit:int=10, db: Session = Depends(get_db())):
    service = ForumService()
    response = service.get_all(db, offset=offset, limit=limit)
    return response

@forum_router.get("{forum_id}", response_model=schemas.Forum)
def get_forum(forum_id:str, db: Session = Depends(get_db)):
    service = ForumService()
    response = service.get(forum_id, db)
    return response

@forum_router.post("/", response_model=schemas.Forum)
def create_forum(forum: schemas.ForumCreate, db: Session = Depends(get_db())):
    service = ForumService()
    new_forum = service.create(forum.model_dump(), db)
    return new_forum

@forum_router.put("/{forum_id}", response_model=schemas.Forum)
def update_forum(forum_id:str, forum: schemas.ForumUpdate, db: Session = Depends(get_db)):
    service = ForumService()
    updated_forum=service.update(forum_id, forum.model_dump(), db)
    return updated_forum

@forum_router.delete("/{forum_id}", response_model=schemas.Forum)
def delete_forum(forum_id:str, db: Session = Depends(get_db)):
    service = ForumService()
    deleted_forum=service.delete(forum_id, db)
    return deleted_forum

#Posts

post_router = APIRouter(
    prefix="/post",
    tags=["posts"]
)

@post_router.post("/", response_model=schemas.Post)
def create_post(post: schemas.PostCreate, db: Session = Depends(get_db)):
    service = PostService()
    post = service.create(post.model_dump(), db)
    return post

@post_router.get("/{post_id}", response_model=schemas.Post)
def get_post(post_id:str, db: Session = Depends(get_db)):
    service = PostService()
    post = service.get(post_id, db)
    return post

@post_router.delete("/{post_id}", response_model=schemas.Post)
def delete_post(post_id:str, db: Session = Depends(get_db)):
    service = PostService()
    deleted_post=service.delete(post_id, db)
    return deleted_post

