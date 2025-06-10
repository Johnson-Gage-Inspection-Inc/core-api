from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue
from office365.runtime.client_value_collection import (
    ClientValueCollection as ClientValueCollection,
)
from office365.sharepoint.publishing.diagnostics.page_result import (
    PageDiagnosticsResult as PageDiagnosticsResult,
)

class PageDiagnostics(ClientValue):
    Results: Incomplete
    def __init__(self, results: Incomplete | None = None) -> None: ...
    @property
    def entity_type_name(self): ...
