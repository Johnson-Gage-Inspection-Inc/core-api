from _typeshed import Incomplete
from office365.entity_collection import EntityCollection as EntityCollection
from office365.onedrive.workbooks.names.named_item import WorkbookNamedItem as WorkbookNamedItem
from office365.runtime.queries.service_operation import ServiceOperationQuery as ServiceOperationQuery

class WorkbookNamedItemCollection(EntityCollection[WorkbookNamedItem]):
    def __init__(self, context, resource_path: Incomplete | None = None) -> None: ...
    def add(self, name, reference, comment: Incomplete | None = None): ...
