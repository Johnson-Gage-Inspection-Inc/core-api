from office365.entity import Entity as Entity
from office365.runtime.client_result import ClientResult as ClientResult
from office365.runtime.queries.service_operation import (
    ServiceOperationQuery as ServiceOperationQuery,
)
from office365.runtime.types.collections import StringCollection as StringCollection

class ApplicationTemplate(Entity):
    def instantiate(self, display_name): ...
    @property
    def display_name(self) -> str | None: ...
    @property
    def categories(self): ...
    @property
    def supported_provisioning_types(self): ...
    @property
    def supported_single_signon_modes(self): ...
