from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue
from office365.runtime.client_value_collection import (
    ClientValueCollection as ClientValueCollection,
)
from office365.sharepoint.search.special_term_result import (
    SpecialTermResult as SpecialTermResult,
)

class SpecialTermResults(ClientValue):
    Results: Incomplete
    def __init__(self, results: Incomplete | None = None) -> None: ...
    @property
    def entity_type_name(self): ...
