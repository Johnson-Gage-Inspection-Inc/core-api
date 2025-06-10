from _typeshed import Incomplete
from office365.runtime.queries.service_operation import (
    ServiceOperationQuery as ServiceOperationQuery,
)
from office365.sharepoint.authpolicy.events.event import SPAuthEvent as SPAuthEvent
from office365.sharepoint.entity_collection import EntityCollection as EntityCollection

class SPAuthEventCollection(EntityCollection[SPAuthEvent]):
    def __init__(
        self,
        context,
        resource_path: Incomplete | None = None,
        parent: Incomplete | None = None,
    ) -> None: ...
    def role_assignment_ms_graph_notify(
        self, tenant, action, type_, resource_payload, id_, container_id
    ): ...
