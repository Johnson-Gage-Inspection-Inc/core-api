from _typeshed import Incomplete
from office365.entity import Entity as Entity
from office365.entity_collection import EntityCollection as EntityCollection
from office365.onedrive.sitepages.webparts.web_part import WebPart as WebPart
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath

class HorizontalSectionColumn(Entity):
    @property
    def web_parts(self) -> EntityCollection[WebPart]: ...
    def get_property(self, name, default_value: Incomplete | None = None): ...
