from _typeshed import Incomplete
from office365.entity_collection import EntityCollection as EntityCollection
from office365.onedrive.workbooks.tables.columns.column import (
    WorkbookTableColumn as WorkbookTableColumn,
)
from office365.runtime.client_result import ClientResult as ClientResult
from office365.runtime.queries.function import FunctionQuery as FunctionQuery

class WorkbookTableColumnCollection(EntityCollection[WorkbookTableColumn]):
    def __init__(self, context, resource_path: Incomplete | None = None) -> None: ...
    def add(self, index, name, values: Incomplete | None = None): ...
    def count(self): ...
