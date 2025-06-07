from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue
from office365.runtime.client_value_collection import ClientValueCollection as ClientValueCollection
from office365.sharepoint.search.endpoints import SearchEndpoints as SearchEndpoints

class QueryRoutingInfo(ClientValue):
    QueryState: Incomplete
    SearchEndpoints: Incomplete
    def __init__(self, query_state: Incomplete | None = None, search_endpoints: Incomplete | None = None) -> None: ...
    @property
    def entity_type_name(self): ...
