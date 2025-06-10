from office365.runtime.paths.resource_path import ResourcePath as ResourcePath

class AppIdPath(ResourcePath):
    @property
    def segment(self): ...
    @property
    def delimiter(self) -> None: ...
