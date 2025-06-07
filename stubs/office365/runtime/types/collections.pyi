from _typeshed import Incomplete
from office365.runtime.client_value_collection import ClientValueCollection as ClientValueCollection

class StringCollection(ClientValueCollection[str]):
    def __init__(self, initial_values: Incomplete | None = None) -> None: ...

class GuidCollection(ClientValueCollection):
    def __init__(self, initial_values: Incomplete | None = None) -> None: ...
