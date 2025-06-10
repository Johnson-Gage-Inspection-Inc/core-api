from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class OnenoteOperationError(ClientValue):
    message: Incomplete
    code: Incomplete
    def __init__(
        self, message: Incomplete | None = None, code: Incomplete | None = None
    ) -> None: ...
