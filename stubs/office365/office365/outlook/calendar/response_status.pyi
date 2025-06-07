from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class ResponseStatus(ClientValue):
    response: Incomplete
    def __init__(self, response: Incomplete | None = None) -> None: ...
