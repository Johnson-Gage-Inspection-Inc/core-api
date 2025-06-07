from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class AppIdentity(ClientValue):
    appId: Incomplete
    displayName: Incomplete
    servicePrincipalId: Incomplete
    servicePrincipalName: Incomplete
    def __init__(
        self,
        app_id: Incomplete | None = None,
        display_name: Incomplete | None = None,
        service_principal_id: Incomplete | None = None,
        service_principal_name: Incomplete | None = None,
    ) -> None: ...
