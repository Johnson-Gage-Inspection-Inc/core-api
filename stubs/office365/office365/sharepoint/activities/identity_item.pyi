from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class ActivityIdentityItem(ClientValue):
    clientId: Incomplete
    clientIdProvider: Incomplete
    displayName: Incomplete
    email: Incomplete
    userPrincipalName: Incomplete
    def __init__(
        self,
        client_id: Incomplete | None = None,
        clientIdProvider: Incomplete | None = None,
        displayName: Incomplete | None = None,
        email: Incomplete | None = None,
        userPrincipalName: Incomplete | None = None,
    ) -> None: ...
    @property
    def entity_type_name(self): ...
