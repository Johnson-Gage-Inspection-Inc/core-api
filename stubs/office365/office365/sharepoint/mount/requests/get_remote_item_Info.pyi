from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue
from office365.runtime.types.collections import StringCollection as StringCollection

class GetRemoteItemInfoRequest(ClientValue):
    RemoteItemUniqueIds: Incomplete
    def __init__(self, RemoteItemUniqueIds: Incomplete | None = None) -> None: ...
    @property
    def entity_type_name(self): ...
