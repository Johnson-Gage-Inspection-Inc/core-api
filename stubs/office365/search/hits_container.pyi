from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue
from office365.runtime.client_value_collection import ClientValueCollection as ClientValueCollection
from office365.search.aggregation import SearchAggregation as SearchAggregation
from office365.search.hit import SearchHit as SearchHit

class SearchHitsContainer(ClientValue):
    hits: Incomplete
    moreResultsAvailable: Incomplete
    total: Incomplete
    aggregations: Incomplete
    def __init__(self, hits: Incomplete | None = None, more_results_available: Incomplete | None = None, total: Incomplete | None = None, aggregations: Incomplete | None = None) -> None: ...
