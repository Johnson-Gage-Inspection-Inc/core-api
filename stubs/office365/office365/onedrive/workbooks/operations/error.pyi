from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class WorkbookOperationError(ClientValue):
    code: Incomplete
    innerError: Incomplete
    message: Incomplete
    def __init__(
        self,
        code: Incomplete | None = None,
        innerError: Incomplete | None = None,
        message: Incomplete | None = None,
    ) -> None: ...
