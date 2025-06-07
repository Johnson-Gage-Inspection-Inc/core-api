from _typeshed import Incomplete
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath
from office365.sharepoint.entity import Entity as Entity

class AnnouncementsController(Entity):
    def __init__(self, context, path: Incomplete | None = None) -> None: ...
    @property
    def entity_type_name(self): ...
