from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class SPClientSideComponentIdentifier(ClientValue):
    id: Incomplete
    version: Incomplete
    def __init__(
        self, _id: Incomplete | None = None, version: Incomplete | None = None
    ) -> None: ...
    @property
    def entity_type_name(self): ...
