from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue
from office365.runtime.client_value_collection import ClientValueCollection as ClientValueCollection

class CollaborativeUsers(ClientValue):
    @property
    def entity_type_name(self): ...

class CollaborationInsightsData(ClientValue):
    collaborativeUsers: Incomplete
    lastReportDate: Incomplete
    def __init__(self, last_report_date: Incomplete | None = None, collaborative_users: Incomplete | None = None) -> None: ...
    @property
    def entity_type_name(self): ...
