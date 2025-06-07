from _typeshed import Incomplete
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath
from office365.runtime.paths.v4.entity import EntityPath as EntityPath

class SharedPath(EntityPath):
    __class__: Incomplete
    def patch(self, key): ...
    @property
    def segment(self): ...
