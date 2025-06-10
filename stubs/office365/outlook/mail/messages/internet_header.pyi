from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class InternetMessageHeader(ClientValue):
    name: Incomplete
    value: Incomplete
    def __init__(
        self, name: Incomplete | None = None, value: Incomplete | None = None
    ) -> None: ...
