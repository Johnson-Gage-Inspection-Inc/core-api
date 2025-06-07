from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class DefaultColumnValue(ClientValue):
    formula: Incomplete
    value: Incomplete
    def __init__(self, formula: Incomplete | None = None, value: Incomplete | None = None) -> None: ...
