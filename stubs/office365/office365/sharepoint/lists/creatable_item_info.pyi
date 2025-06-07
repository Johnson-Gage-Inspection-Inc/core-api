from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue
from office365.runtime.client_value_collection import (
    ClientValueCollection as ClientValueCollection,
)

class CreatableItemInfo(ClientValue): ...

class CreatableItemInfoCollection(ClientValue):
    Items: Incomplete
    def __init__(self, items: Incomplete | None = None) -> None: ...
