from pydantic import BaseModel, Field
from typing import Optional, Dict, Any
from datetime import datetime


class ForumBase(BaseModel):
    name: str = Field(..., max_length=64)
    description: str = Field(..., max_length=255)


class ForumCreate(ForumBase):
    def model_dump(self) -> Dict[str, Any]:
        return super().model_dump(exclude_unset=True)


class ForumUpdate(BaseModel):
    name: Optional[str] = Field(None, max_length=64)
    description: Optional[str] = Field(None, max_length=255)

    def model_dump(self) -> Dict[str, Any]:
        return super().model_dump(exclude_unset=True, exclude_none=True)


class Forum(ForumBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class PostBase(BaseModel):
    name: Optional[str] = Field(None, max_length=64)
    type: str = Field(..., max_length=64)
    content: str = Field(..., max_length=1024)
    forum_id: int
    parent_post_id: Optional[int] = None


class PostCreate(PostBase):
    def model_dump(self) -> Dict[str, Any]:
        return super().model_dump(exclude_unset=True)


class PostUpdate(BaseModel):
    name: Optional[str] = Field(None, max_length=64)
    type: Optional[str] = Field(None, max_length=64)
    content: Optional[str] = Field(None, max_length=1024)
    forum_id: Optional[int] = None
    parent_post_id: Optional[int] = None

    def model_dump(self) -> Dict[str, Any]:
        return super().model_dump(exclude_unset=True, exclude_none=True)


class Post(PostBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True