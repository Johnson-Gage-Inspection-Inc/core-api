from office365.runtime.client_result import ClientResult as ClientResult
from office365.runtime.paths.service_operation import (
    ServiceOperationPath as ServiceOperationPath,
)
from office365.runtime.queries.service_operation import (
    ServiceOperationQuery as ServiceOperationQuery,
)
from office365.sharepoint.entity import Entity as Entity

class ListTemplate(Entity):
    def get_global_schema_xml(self): ...
    @property
    def internal_name(self) -> str | None: ...
    def set_property(self, name, value, persist_changes: bool = True): ...
