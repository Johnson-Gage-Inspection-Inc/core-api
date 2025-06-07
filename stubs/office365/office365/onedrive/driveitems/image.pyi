from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class Image(ClientValue):
    height: Incomplete
    width: Incomplete
    def __init__(
        self, height: Incomplete | None = None, width: Incomplete | None = None
    ) -> None: ...
