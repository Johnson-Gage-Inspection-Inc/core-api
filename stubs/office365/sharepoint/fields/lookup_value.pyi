from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class FieldLookupValue(ClientValue):
    LookupId: Incomplete
    LookupValue: Incomplete
    def __init__(self, lookup_id: Incomplete | None = None, lookup_value: Incomplete | None = None) -> None: ...
    @property
    def entity_type_name(self): ...
