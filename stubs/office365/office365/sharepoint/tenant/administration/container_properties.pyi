from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class SPContainerProperties(ClientValue):
    AllowEditing: Incomplete
    AuthenticationContextName: Incomplete
    def __init__(
        self,
        AllowEditing: Incomplete | None = None,
        AuthenticationContextName: Incomplete | None = None,
    ) -> None: ...
    @property
    def entity_type_name(self): ...
