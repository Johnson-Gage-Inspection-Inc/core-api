from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue
from office365.sharepoint.lists.collection_position import (
    ListCollectionPosition as ListCollectionPosition,
)

class GetListsParameters(ClientValue):
    ListCollectionPosition: Incomplete
    RowLimit: Incomplete
    def __init__(self, position=..., row_limit: int = 100) -> None: ...
    @property
    def entity_type_name(self): ...
