from _typeshed import Incomplete
from office365.entity import Entity as Entity
from office365.entity_collection import EntityCollection as EntityCollection
from office365.onedrive.workbooks.charts.chart import WorkbookChart as WorkbookChart
from office365.onedrive.workbooks.names.named_item import (
    WorkbookNamedItem as WorkbookNamedItem,
)
from office365.onedrive.workbooks.ranges.range import WorkbookRange as WorkbookRange
from office365.onedrive.workbooks.tables.collection import (
    WorkbookTableCollection as WorkbookTableCollection,
)
from office365.onedrive.workbooks.tables.pivot_table_collection import (
    WorkbookPivotTableCollection as WorkbookPivotTableCollection,
)
from office365.onedrive.workbooks.worksheets.protection import (
    WorkbookWorksheetProtection as WorkbookWorksheetProtection,
)
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath
from office365.runtime.queries.function import FunctionQuery as FunctionQuery

class WorkbookWorksheet(Entity):
    def cell(self, row, column): ...
    def range(self, address: Incomplete | None = None): ...
    def used_range(self, values_only: bool = False): ...
    @property
    def charts(self) -> EntityCollection[WorkbookChart]: ...
    @property
    def name(self) -> str | None: ...
    @property
    def names(self) -> EntityCollection[WorkbookNamedItem]: ...
    @property
    def tables(self) -> WorkbookTableCollection: ...
    @property
    def pivot_tables(self) -> WorkbookPivotTableCollection: ...
    @property
    def protection(self) -> WorkbookWorksheetProtection: ...
    def get_property(self, name, default_value: Incomplete | None = None): ...
