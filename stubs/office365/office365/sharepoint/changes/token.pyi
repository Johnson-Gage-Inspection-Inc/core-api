from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class ChangeToken(ClientValue):
    StringValue: Incomplete
    def __init__(self, string_value: Incomplete | None = None) -> None: ...
    @property
    def entity_type_name(self): ...
