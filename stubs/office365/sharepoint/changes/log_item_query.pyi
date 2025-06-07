from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class ChangeLogItemQuery(ClientValue):
    Query: Incomplete
    QueryOptions: Incomplete
    ChangeToken: Incomplete
    Contains: Incomplete
    RowLimit: Incomplete
    def __init__(self, change_token: Incomplete | None = None, query: Incomplete | None = None, query_options: Incomplete | None = None, contains: Incomplete | None = None, row_limit: Incomplete | None = None) -> None: ...
    @property
    def entity_type_name(self): ...
