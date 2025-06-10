from office365.runtime.queries.service_operation import (
    ServiceOperationQuery as ServiceOperationQuery,
)
from office365.sharepoint.client_context import ClientContext as ClientContext
from office365.sharepoint.entity import Entity as Entity
from office365.sharepoint.flows.connector_result import (
    ConnectorResult as ConnectorResult,
)

class FormsCustomization(Entity):
    @staticmethod
    def can_customize_forms(
        context: ClientContext,
        list_name: str,
        return_type: ConnectorResult | None = None,
    ) -> ConnectorResult: ...
    @property
    def entity_type_name(self): ...
