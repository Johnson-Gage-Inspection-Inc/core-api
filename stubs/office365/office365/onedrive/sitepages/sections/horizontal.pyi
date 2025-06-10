from office365.entity import Entity as Entity
from office365.entity_collection import EntityCollection as EntityCollection
from office365.onedrive.sitepages.sections.horizontal_column import (
    HorizontalSectionColumn as HorizontalSectionColumn,
)
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath

class HorizontalSection(Entity):
    @property
    def columns(self) -> EntityCollection[HorizontalSectionColumn]: ...
