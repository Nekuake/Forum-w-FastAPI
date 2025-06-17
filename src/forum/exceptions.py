from fastapi import HTTPException

class EntityRemovedException(HTTPException):
    def __init__(self, id:str ):
        super().__init__(status_code=404, detail=f"Tried to interact with removed entity: ID {id}")

class UserNotPrivilegedException(HTTPException):
    def __init__(self, id: str):
        super().__init__(status_code=403, detail="Tried to perform privileged actions with no authorization.")

class TriedToUpdateNonExistentField(HTTPException):
    def __init__(self, field_name: str):
        super().__init__(status_code=400, detail=f"Tried to interact with unknown field: Field name {field_name}")

class TriedToDeleteNonExistentEntity(HTTPException):
    def __init__(self, id: str):
        super().__init__(status_code=404, detail=f"Tried to remove unknown entity: ID {id}")

class EntityNotFoundException(HTTPException):
    def __init__(self, id:str):
        super().__init__(status_code=404, detail=f"Entity not found: ID {id}")
