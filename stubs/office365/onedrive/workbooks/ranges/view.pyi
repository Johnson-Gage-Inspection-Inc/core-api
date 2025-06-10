from office365.entity import Entity as Entity
from office365.entity_collection import EntityCollection as EntityCollection
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath

class WorkbookRangeView(Entity):
    @property
    def cell_addresses(self) -> dict | None: ...
    @property
    def column_count(self) -> int | None: ...
    @property
    def rows(self) -> EntityCollection[WorkbookRangeView]: ...
