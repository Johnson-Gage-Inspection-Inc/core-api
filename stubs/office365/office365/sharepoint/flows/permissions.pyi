from office365.runtime.queries.service_operation import (
    ServiceOperationQuery as ServiceOperationQuery,
)
from office365.sharepoint.client_context import ClientContext as ClientContext
from office365.sharepoint.entity import Entity as Entity
from office365.sharepoint.flows.connector_result import (
    ConnectorResult as ConnectorResult,
)

class FlowPermissions(Entity):
    @staticmethod
    def get_flow_permission_level_on_list(
        context: ClientContext,
        list_name: str,
        return_type: ConnectorResult | None = None,
    ) -> ConnectorResult: ...
    @property
    def entity_type_name(self): ...
