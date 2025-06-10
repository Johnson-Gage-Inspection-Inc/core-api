from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue
from office365.runtime.client_value_collection import (
    ClientValueCollection as ClientValueCollection,
)
from office365.sharepoint.publishing.portal_health_details import (
    PortalHealthDetails as PortalHealthDetails,
)

class PortalHealthStatus(ClientValue):
    Details: Incomplete
    Status: Incomplete
    def __init__(
        self, details: Incomplete | None = None, status: Incomplete | None = None
    ) -> None: ...
    @property
    def entity_type_name(self): ...
