from sqlalchemy.orm import Session
from sqlalchemy import and_

from src.forum.exceptions import TriedToUpdateNonExistentField
from src.forum.models import Forum, Post
from typing import Generic, TypeVar, Type, List, Optional, Dict, Any, Union
from src.database import get_db, Base
import logging


log=logging.getLogger(__name__)
ModelType = TypeVar("ModelType", bound=Base)
class BaseService:
    def __init__(self, model):
        self.db = get_db()
        self.model = model


    def create(self, obj_in: Dict[str, Any]) -> ModelType:
        db_obj = self.model(**obj_in)
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj


    def get(self, id: int, filters=None, offset:int=0, limit:int=1) -> Optional[ModelType]:
        filters["deleted"] = False
        return self.db.query(self.model).filter(self.model.id == id).filter(*filters).offset(offset).limit(limit)


    def update(self, id: int, obj_in: Dict[str, Any]) -> Optional[ModelType]:
        db_obj = self.get(id)
        if db_obj:
            for field, value in obj_in.items():
                if hasattr(db_obj, field):
                    setattr(db_obj, field, value)
                else:
                    self.db.rollback()
                    raise TriedToUpdateNonExistentField(field)

            self.db.commit()
            self.db.refresh(db_obj)
        return db_obj

    def delete(self, id: int) -> bool:
        db_obj = self.get(id)
        if db_obj:
            self.db.delete(db_obj)
            self.db.commit()
            return True
        return False


class ForumService(BaseService):
    def __init__(self):
        super().__init__(Forum)

class PostService(BaseService):
    def __init__(self):
        super().__init__(Post)


