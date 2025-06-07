from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class Identity(ClientValue):
    displayName: Incomplete
    id: Incomplete
    def __init__(
        self, display_name: Incomplete | None = None, _id: Incomplete | None = None
    ) -> None: ...
