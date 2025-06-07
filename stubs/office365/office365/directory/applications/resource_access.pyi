from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class ResourceAccess(ClientValue):
    id: Incomplete
    type: Incomplete
    def __init__(
        self, id_: Incomplete | None = None, type_: Incomplete | None = None
    ) -> None: ...
    @property
    def type_name(self): ...
