from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from src.forum import schemas
from src.forum.service import PostService, ForumService

forum_router = APIRouter()

@forum_router.get("/", response_model=List)