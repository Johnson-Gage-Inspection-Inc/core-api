from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class SharingLinkAccessRequest(ClientValue):
    ensureAccess: Incomplete
    password: Incomplete
    def __init__(
        self,
        ensure_access: Incomplete | None = None,
        password: Incomplete | None = None,
    ) -> None: ...
    @property
    def entity_type_name(self): ...
