from office365.runtime.queries.service_operation import (
    ServiceOperationQuery as ServiceOperationQuery,
)
from office365.sharepoint.entity import Entity as Entity

class MySiteDismissStatusText(Entity):
    @staticmethod
    def dismiss_status_text(context): ...
    @property
    def entity_type_name(self): ...
