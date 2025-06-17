from src.forum.exceptions import (TriedToUpdateNonExistentField,
                                  EntityRemovedException,
                                  EntityNotFoundException)
from src.forum.models import Forum, Post
from typing import TypeVar, List, Dict, Any
from src.database import  Base
import logging


log=logging.getLogger(__name__)
ModelType = TypeVar("ModelType", bound=Base)
class BaseService:
    def __init__(self, model):
        self.model = model


    def create(self, obj_in: Dict[str, Any], db) -> ModelType:
        db_obj = self.model(**obj_in)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj


    def get_all(self, db, filters=None, offset:int=0, limit:int=1) -> List[ModelType]:
        filters["deleted"] = False
        return db.query(self.model).filter(*filters).offset(offset).limit(limit).all()

    def get(self, id:str, db) -> ModelType:
        entity_object = db.query(self.model).get(id)
        if entity_object:
            if entity_object.deleted:
                raise EntityRemovedException(id)
            else: return entity_object
        else: raise EntityNotFoundException(id)


    def update(self, id: str, obj_in: Dict[str, Any], db):
        db_obj = self.get(id, db)
        if db_obj:
            for field, value in obj_in.items():
                if hasattr(db_obj, field):
                    setattr(db_obj, field, value)
                else:
                    db.rollback()
                    raise TriedToUpdateNonExistentField(field)

            db.commit()
            db.refresh(db_obj)
        return db_obj

    def delete(self, id: str, db):
        db_obj = self.get(id, db)
        if db_obj:
            db_obj.deleted = True
            db.commit()
            return db_obj  # Return the deleted object
        else:
            raise EntityNotFoundException(id)


class ForumService(BaseService):
    def __init__(self):
        super().__init__(Forum)

class PostService(BaseService):
    def __init__(self):
        super().__init__(Post)


