from office365.runtime.paths.resource_path import ResourcePath as ResourcePath

class EntityPath(ResourcePath):
    @property
    def segment(self): ...
    @property
    def delimiter(self) -> None: ...
