from office365.runtime.client_value_collection import (
    ClientValueCollection as ClientValueCollection,
)
from office365.runtime.queries.service_operation import (
    ServiceOperationQuery as ServiceOperationQuery,
)
from office365.sharepoint.entity import Entity as Entity
from office365.sharepoint.search.query.sort.sort import Sort as Sort

class SortCollection(Entity):
    def add(self, property_name, direction): ...
    def clear(self): ...
    @property
    def items(self): ...
    @property
    def entity_type_name(self): ...
