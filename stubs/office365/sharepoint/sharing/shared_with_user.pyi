from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class SharedWithUser(ClientValue):
    Email: Incomplete
    Name: Incomplete
    def __init__(
        self, email: Incomplete | None = None, name: Incomplete | None = None
    ) -> None: ...
