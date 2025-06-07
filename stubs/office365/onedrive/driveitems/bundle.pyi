from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class Bundle(ClientValue):
    album: Incomplete
    childCount: Incomplete
    def __init__(self, album: Incomplete | None = None, child_count: Incomplete | None = None) -> None: ...
