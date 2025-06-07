from _typeshed import Incomplete
from office365.entity import Entity as Entity
from office365.entity_collection import EntityCollection as EntityCollection
from office365.onedrive.sitepages.sections.horizontal import HorizontalSection as HorizontalSection
from office365.onedrive.sitepages.sections.vertical import VerticalSection as VerticalSection
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath

class CanvasLayout(Entity):
    @property
    def horizontal_sections(self) -> EntityCollection[HorizontalSection]: ...
    @property
    def vertical_section(self) -> VerticalSection: ...
    def get_property(self, name, default_value: Incomplete | None = None): ...
