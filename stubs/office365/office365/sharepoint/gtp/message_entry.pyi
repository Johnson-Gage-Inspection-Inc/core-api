from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class MessageEntry(ClientValue):
    content: Incomplete
    def __init__(self, content: Incomplete | None = None) -> None: ...
    @property
    def entity_type_name(self): ...
