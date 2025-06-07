from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class ListCollectionPosition(ClientValue):
    PagingInfo: Incomplete
    def __init__(self, paging_info: str = 'Paged=TRUE&p_ID=0') -> None: ...
    @property
    def entity_type_name(self): ...
