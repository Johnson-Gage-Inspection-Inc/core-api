from _typeshed import Incomplete
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath
from office365.sharepoint.entity import Entity as Entity

class VivaSiteManager(Entity):
    def __init__(self, content, resource_path: Incomplete | None = None) -> None: ...
    @property
    def entity_type_name(self): ...
