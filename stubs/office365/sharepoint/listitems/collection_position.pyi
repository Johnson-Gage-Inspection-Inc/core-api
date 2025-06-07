from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class ListItemCollectionPosition(ClientValue):
    PagingInfo: Incomplete
    def __init__(self, paging_info: Incomplete | None = None) -> None: ...
    @property
    def entity_type_name(self): ...
