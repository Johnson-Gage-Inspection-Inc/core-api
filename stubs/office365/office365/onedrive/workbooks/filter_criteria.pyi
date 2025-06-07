from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class WorkbookFilterCriteria(ClientValue):
    color: Incomplete
    dynamicCriteria: Incomplete
    operator: Incomplete
    values: Incomplete
    def __init__(
        self,
        color: Incomplete | None = None,
        dynamic_criteria: Incomplete | None = None,
        operator: Incomplete | None = None,
        values: Incomplete | None = None,
    ) -> None: ...
