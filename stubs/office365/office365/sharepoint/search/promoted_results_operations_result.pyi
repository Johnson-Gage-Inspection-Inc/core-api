from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue
from office365.runtime.client_value_collection import (
    ClientValueCollection as ClientValueCollection,
)
from office365.sharepoint.search.object_owner_result import (
    SearchObjectOwnerResult as SearchObjectOwnerResult,
)
from office365.sharepoint.search.promoted_result_query_rule import (
    PromotedResultQueryRule as PromotedResultQueryRule,
)

class PromotedResultsOperationsResult(ClientValue):
    Result: Incomplete
    SearchObjectOwner: Incomplete
    def __init__(self, result: Incomplete | None = None, object_owner=...) -> None: ...
    @property
    def entity_type_name(self): ...
