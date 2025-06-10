from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class SpecialFolder(ClientValue):
    name: Incomplete
    def __init__(self, name: Incomplete | None = None) -> None: ...
