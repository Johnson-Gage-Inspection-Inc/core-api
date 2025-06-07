from office365.runtime.client_result import ClientResult as ClientResult
from office365.runtime.client_value_collection import (
    ClientValueCollection as ClientValueCollection,
)
from office365.runtime.queries.service_operation import (
    ServiceOperationQuery as ServiceOperationQuery,
)
from office365.sharepoint.entity import Entity as Entity
from office365.sharepoint.translation.resource_entry import (
    SPResourceEntry as SPResourceEntry,
)

class UserResource(Entity):
    def get_value_for_ui_culture(self, culture_name): ...
    def get_resource_entries(self): ...
    def set_value_for_ui_culture(self, culture_name, value): ...
