from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue
from office365.runtime.client_value_collection import ClientValueCollection as ClientValueCollection
from office365.search.bucket import SearchBucket as SearchBucket

class SearchAggregation(ClientValue):
    buckets: Incomplete
    field: Incomplete
    def __init__(self, buckets: Incomplete | None = None, field: Incomplete | None = None) -> None: ...
