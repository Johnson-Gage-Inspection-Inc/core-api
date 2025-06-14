from office365.runtime.client_result import ClientResult as ClientResult
from office365.runtime.queries.service_operation import (
    ServiceOperationQuery as ServiceOperationQuery,
)
from office365.sharepoint.entity import Entity as Entity

class ThemeManager(Entity):
    @property
    def entity_type_name(self): ...
    def add_tenant_theme(self, name, theme_json): ...
    def delete_tenant_theme(self, name): ...
