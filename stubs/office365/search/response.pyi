from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue
from office365.runtime.client_value_collection import (
    ClientValueCollection as ClientValueCollection,
)
from office365.runtime.types.collections import StringCollection as StringCollection
from office365.search.hits_container import SearchHitsContainer as SearchHitsContainer

class SearchResponse(ClientValue):
    searchTerms: Incomplete
    hitsContainers: Incomplete
    def __init__(
        self,
        search_terms: Incomplete | None = None,
        hits_containers: Incomplete | None = None,
    ) -> None: ...
