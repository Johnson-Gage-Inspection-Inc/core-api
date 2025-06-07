from _typeshed import Incomplete
from office365.entity_collection import EntityCollection as EntityCollection
from office365.onedrive.workbooks.worksheets.worksheet import WorkbookWorksheet as WorkbookWorksheet
from office365.runtime.queries.service_operation import ServiceOperationQuery as ServiceOperationQuery

class WorkbookWorksheetCollection(EntityCollection[WorkbookWorksheet]):
    def __init__(self, context, resource_path: Incomplete | None = None) -> None: ...
    def add(self, name: Incomplete | None = None): ...
