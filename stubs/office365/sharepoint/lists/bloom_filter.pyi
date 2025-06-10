from office365.runtime.client_value_collection import (
    ClientValueCollection as ClientValueCollection,
)
from office365.sharepoint.entity import Entity as Entity

class ListBloomFilter(Entity):
    @property
    def bloom_filter_size(self) -> int | None: ...
    @property
    def index_map(self): ...
