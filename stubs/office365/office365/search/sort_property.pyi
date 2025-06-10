from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class SortProperty(ClientValue):
    isDescending: Incomplete
    name: Incomplete
    def __init__(
        self, is_descending: Incomplete | None = None, name: Incomplete | None = None
    ) -> None: ...
