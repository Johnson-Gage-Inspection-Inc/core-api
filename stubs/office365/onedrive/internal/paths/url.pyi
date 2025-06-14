from office365.onedrive.internal.paths.root import RootPath as RootPath
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath
from office365.runtime.paths.v4.entity import EntityPath as EntityPath
from typing_extensions import Self

class UrlPath(EntityPath):
    def __init__(
        self, url: str, parent: ResourcePath, collection: ResourcePath = None
    ) -> None: ...
    def patch(self, key: str) -> Self: ...
    @property
    def segment(self): ...
    @property
    def delimiter(self) -> None: ...
