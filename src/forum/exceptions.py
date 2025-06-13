class BlogRemovedException(Exception):
    pass

class PostRemovedException(Exception):
    pass

class UserNotPrivilegedException(Exception):
    pass

class TriedToUpdateNonExistentField(Exception):
    pass