from http.client import responses

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from src.forum import schemas
from src.forum.service import PostService, ForumService
from src.database import get_db, Base



#Forum
forum_router = APIRouter(
    prefix="/forums",
    tags=["forums"]
)

@forum_router.get("/", response_model=List)
def get_forums(offset:int=0, limit:int=10, db: Session = Depends(get_db())):
    service = ForumService()
    response = service.get_all(offset=offset, limit=limit)
    return response

@forum_router.get("{forum_id}", response_model=schemas.Forum)
def get_forum(forum_id:str, db: Session = Depends(get_db)):
    service = ForumService()
    response = service.get(forum_id)
    return response

@forum_router.post("/", response_model=schemas.Forum)
def create_forum(forum: schemas.ForumCreate, db: Session = Depends(get_db())):
    service = ForumService()
    new_forum = service.create(forum.model_dump())
    return new_forum

@forum_router.put("/{forum_id}", response_model=schemas.Forum)
def update_forum(forum_id:str, forum: schemas.ForumUpdate, db: Session = Depends(get_db)):
    service = ForumService()
    updated_forum=service.update(forum_id, forum.model_dump())
    return updated_forum


def delete_forum(forum_id:str, db: Session = Depends(get_db)):
    service = ForumService()
    deleted_forum=service.delete(forum_id)
    return deleted_forum

#Posts