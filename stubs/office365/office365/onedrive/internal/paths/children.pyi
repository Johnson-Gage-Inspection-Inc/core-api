from _typeshed import Incomplete
from office365.runtime.paths.v4.entity import EntityPath as EntityPath

class ChildrenPath(EntityPath):
    def __init__(self, parent, collection: Incomplete | None = None) -> None: ...
    @property
    def collection(self): ...
