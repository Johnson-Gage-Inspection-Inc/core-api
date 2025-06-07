from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue
from office365.runtime.client_value_collection import (
    ClientValueCollection as ClientValueCollection,
)
from office365.sharepoint.search.simple_data_row import SimpleDataRow as SimpleDataRow

class SimpleDataTable(ClientValue):
    Rows: Incomplete
    def __init__(self, rows: Incomplete | None = None) -> None: ...
    @property
    def entity_type_name(self): ...
