from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class SearchQuery(ClientValue):
    queryString: Incomplete
    queryTemplate: Incomplete
    def __init__(self, query_string: Incomplete | None = None, query_template: Incomplete | None = None) -> None: ...
