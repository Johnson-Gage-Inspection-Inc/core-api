from _typeshed import Incomplete
from office365.entity import Entity as Entity
from office365.onedrive.workbooks.filter_criteria import (
    WorkbookFilterCriteria as WorkbookFilterCriteria,
)
from office365.runtime.queries.service_operation import (
    ServiceOperationQuery as ServiceOperationQuery,
)

class WorkbookFilter(Entity):
    def apply_bottom_items_filter(self, count: Incomplete | None = None): ...
    def clear(self): ...
    @property
    def criteria(self) -> WorkbookFilterCriteria | None: ...
