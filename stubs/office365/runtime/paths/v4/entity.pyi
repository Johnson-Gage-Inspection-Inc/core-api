from _typeshed import Incomplete
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath
from typing_extensions import Self

class EntityPath(ResourcePath):
    def __init__(
        self,
        key: str | None = None,
        parent: ResourcePath | None = None,
        collection: ResourcePath | None = None,
    ) -> None: ...
    @property
    def collection(self): ...
    @property
    def segment(self): ...
    __class__: Incomplete
    def patch(self, key: str) -> Self: ...
