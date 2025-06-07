from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class RecentAdminActionReport(ClientValue):
    actions: Incomplete
    createdByEmail: Incomplete
    def __init__(self, actions: str = None, created_by_email: str = None) -> None: ...
    @property
    def entity_type_name(self): ...
