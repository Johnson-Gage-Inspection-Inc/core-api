from _typeshed import Incomplete
from office365.runtime.client_value_collection import ClientValueCollection as ClientValueCollection
from office365.sharepoint.search.reports.abandonedqueries.item import ReportAbandonedQueriesItem as ReportAbandonedQueriesItem
from office365.sharepoint.search.reports.base import ReportBase as ReportBase

class ReportAbandonedQueries(ReportBase):
    Reports: Incomplete
    def __init__(self, reports: Incomplete | None = None) -> None: ...
    @property
    def entity_type_name(self): ...
