from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class SiteCreationDefaultStorageQuota(ClientValue):
    IsReadOnly: Incomplete
    Value: Incomplete
    def __init__(self, IsReadOnly: bool = None, Value: int = None) -> None: ...
    @property
    def entity_type_name(self): ...
