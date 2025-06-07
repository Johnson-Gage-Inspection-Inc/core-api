from office365.runtime.client_result import ClientResult as ClientResult
from office365.runtime.paths.service_operation import ServiceOperationPath as ServiceOperationPath
from office365.runtime.queries.service_operation import ServiceOperationQuery as ServiceOperationQuery
from office365.runtime.types.collections import StringCollection as StringCollection
from office365.sharepoint.entity import Entity as Entity

class UserProfilePropertiesForUser(Entity):
    def get_property_names(self): ...
    @property
    def account_name(self) -> str | None: ...
    @property
    def property_names(self): ...
    @property
    def resource_path(self): ...
