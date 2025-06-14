from office365.entity import Entity as Entity
from office365.entity_collection import EntityCollection as EntityCollection
from office365.onedrive.workbooks.ranges.border import (
    WorkbookRangeBorder as WorkbookRangeBorder,
)
from office365.onedrive.workbooks.ranges.fill import (
    WorkbookRangeFill as WorkbookRangeFill,
)
from office365.onedrive.workbooks.ranges.font import (
    WorkbookRangeFont as WorkbookRangeFont,
)
from office365.onedrive.workbooks.ranges.format_protection import (
    WorkbookFormatProtection as WorkbookFormatProtection,
)
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath

class WorkbookRangeFormat(Entity):
    @property
    def column_width(self) -> float | None: ...
    @property
    def horizontal_alignment(self) -> str | None: ...
    @property
    def row_height(self) -> float | None: ...
    @property
    def vertical_alignment(self) -> str | None: ...
    @property
    def wrap_text(self) -> bool | None: ...
    @property
    def borders(self) -> EntityCollection[WorkbookRangeBorder]: ...
    @property
    def fill(self): ...
    @property
    def font(self): ...
    @property
    def protection(self): ...
