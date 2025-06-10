from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class FieldUrlValue(ClientValue):
    Url: Incomplete
    Description: Incomplete
    def __init__(
        self, url: Incomplete | None = None, description: Incomplete | None = None
    ) -> None: ...
    @property
    def entity_type_name(self): ...
