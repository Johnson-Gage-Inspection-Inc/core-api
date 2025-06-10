from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue
from office365.runtime.client_value_collection import (
    ClientValueCollection as ClientValueCollection,
)
from office365.sharepoint.search.reports.topqueries.data import (
    ReportTopQueriesData as ReportTopQueriesData,
)

class ReportTopQueriesItem(ClientValue):
    Date: Incomplete
    Report: Incomplete
    def __init__(
        self, date: Incomplete | None = None, report: Incomplete | None = None
    ) -> None: ...
    @property
    def entity_type_name(self): ...
