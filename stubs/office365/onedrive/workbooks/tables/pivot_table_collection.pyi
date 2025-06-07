from _typeshed import Incomplete
from office365.entity_collection import EntityCollection as EntityCollection
from office365.onedrive.workbooks.tables.pivot_table import WorkbookPivotTable as WorkbookPivotTable
from office365.runtime.queries.service_operation import ServiceOperationQuery as ServiceOperationQuery

class WorkbookPivotTableCollection(EntityCollection[WorkbookPivotTable]):
    def __init__(self, context, resource_path: Incomplete | None = None) -> None: ...
    def refresh_all(self): ...
