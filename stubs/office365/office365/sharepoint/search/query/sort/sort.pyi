from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class Sort(ClientValue):
    Direction: Incomplete
    Property: Incomplete
    def __init__(
        self,
        property_name: Incomplete | None = None,
        direction: Incomplete | None = None,
    ) -> None: ...
    @property
    def entity_type_name(self): ...
