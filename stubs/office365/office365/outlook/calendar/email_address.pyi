from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class EmailAddress(ClientValue):
    address: Incomplete
    name: Incomplete
    def __init__(
        self, address: Incomplete | None = None, name: Incomplete | None = None
    ) -> None: ...
