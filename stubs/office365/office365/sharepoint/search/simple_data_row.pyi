from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue
from office365.runtime.odata.type import ODataType as ODataType

class SimpleDataRow(ClientValue):
    Cells: Incomplete
    def __init__(self, cells: Incomplete | None = None) -> None: ...
    def set_property(self, k, v, persist_changes: bool = True): ...
