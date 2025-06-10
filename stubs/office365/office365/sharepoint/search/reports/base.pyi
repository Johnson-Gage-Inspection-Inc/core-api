from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class ReportBase(ClientValue):
    FarmId: Incomplete
    def __init__(self, farm_id: Incomplete | None = None) -> None: ...
    @property
    def entity_type_name(self): ...
