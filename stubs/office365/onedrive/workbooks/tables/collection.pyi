from _typeshed import Incomplete
from office365.entity_collection import EntityCollection as EntityCollection
from office365.onedrive.workbooks.tables.table import WorkbookTable as WorkbookTable
from office365.runtime.queries.service_operation import ServiceOperationQuery as ServiceOperationQuery

class WorkbookTableCollection(EntityCollection[WorkbookTable]):
    def __init__(self, context, resource_path: Incomplete | None = None) -> None: ...
    def add(self, address, has_headers): ...
