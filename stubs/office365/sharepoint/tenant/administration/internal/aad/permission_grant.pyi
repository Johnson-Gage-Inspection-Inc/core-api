from _typeshed import Incomplete
from office365.runtime.queries.service_operation import (
    ServiceOperationQuery as ServiceOperationQuery,
)
from office365.sharepoint.entity import Entity as Entity
from office365.sharepoint.entity_collection import EntityCollection as EntityCollection
from typing_extensions import Self

class SPO3rdPartyAADPermissionGrant(Entity):
    @property
    def entity_type_name(self): ...

class SPO3rdPartyAADPermissionGrantCollection(
    EntityCollection[SPO3rdPartyAADPermissionGrant]
):
    def __init__(self, context, resource_path: Incomplete | None = None) -> None: ...
    def add(self, service_principal_id: str, resource: str, scope: str) -> Self: ...
