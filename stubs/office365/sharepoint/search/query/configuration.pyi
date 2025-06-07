from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue
from office365.sharepoint.search.endpoints import SearchEndpoints as SearchEndpoints
from office365.sharepoint.search.query.context import QueryContext as QueryContext
from office365.sharepoint.search.query.expanded_parameters import ExpandedQueryParameters as ExpandedQueryParameters
from office365.sharepoint.search.query.routing_info import QueryRoutingInfo as QueryRoutingInfo

class QueryConfiguration(ClientValue):
    QueryContext: Incomplete
    QueryParameters: Incomplete
    QueryRoutingInfo: Incomplete
    SearchEndpoints: Incomplete
    def __init__(self, query_context=..., query_parameters=..., query_routing_info=..., search_endpoints=...) -> None: ...
    @property
    def entity_type_name(self): ...
