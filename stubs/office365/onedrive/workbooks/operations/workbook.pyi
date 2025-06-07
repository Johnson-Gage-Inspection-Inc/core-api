from office365.entity import Entity as Entity
from office365.onedrive.workbooks.operations.error import WorkbookOperationError as WorkbookOperationError

class WorkbookOperation(Entity):
    @property
    def error(self): ...
    @property
    def resource_location(self) -> str | None: ...
    @property
    def status(self) -> str | None: ...
