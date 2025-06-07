from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue
from office365.sharepoint.search.query.context import QueryContext as QueryContext

class SearchEndpoints(ClientValue):
    AdminEndpoint: Incomplete
    QueryContext: Incomplete
    def __init__(self, admin_endpoint: Incomplete | None = None, query_context=...) -> None: ...
    @property
    def entity_type_name(self): ...
