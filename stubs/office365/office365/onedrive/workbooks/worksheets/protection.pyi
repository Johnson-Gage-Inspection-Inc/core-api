from _typeshed import Incomplete
from office365.entity import Entity as Entity
from office365.onedrive.workbooks.worksheets.protection_options import (
    WorkbookWorksheetProtectionOptions as WorkbookWorksheetProtectionOptions,
)
from office365.runtime.queries.service_operation import (
    ServiceOperationQuery as ServiceOperationQuery,
)

class WorkbookWorksheetProtection(Entity):
    def protect(self, options: Incomplete | None = None): ...
    def unprotect(self): ...
    @property
    def options(self): ...
