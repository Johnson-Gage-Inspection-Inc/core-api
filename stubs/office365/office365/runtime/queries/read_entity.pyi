from office365.runtime.odata.query_options import QueryOptions as QueryOptions
from office365.runtime.queries.client_query import ClientQuery as ClientQuery
from office365.runtime.queries.client_query import T as T

class ReadEntityQuery(ClientQuery[T]):
    def __init__(
        self, return_type: T, properties_to_include: list[str] = None
    ) -> None: ...
    @property
    def query_options(self): ...
    @property
    def url(self): ...
