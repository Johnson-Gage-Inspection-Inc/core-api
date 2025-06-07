from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue
from office365.runtime.client_value_collection import (
    ClientValueCollection as ClientValueCollection,
)
from office365.sharepoint.entity import Entity as Entity

class HashTag(ClientValue):
    Name: Incomplete
    UseCount: Incomplete
    def __init__(
        self, name: Incomplete | None = None, use_count: Incomplete | None = None
    ) -> None: ...
    @property
    def entity_type_name(self): ...

class HashTagCollection(Entity):
    @property
    def items(self): ...
