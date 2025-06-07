from office365.runtime.queries.service_operation import (
    ServiceOperationQuery as ServiceOperationQuery,
)
from office365.sharepoint.client_context import ClientContext as ClientContext
from office365.sharepoint.entity import Entity as Entity

class TargetApplication(Entity):
    @staticmethod
    def create(
        context: ClientContext, application_id: str, friendly_name: str
    ) -> TargetApplication: ...
    @property
    def application_id(self) -> str | None: ...
    @property
    def entity_type_name(self): ...
