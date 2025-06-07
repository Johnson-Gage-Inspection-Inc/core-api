from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class Quota(ClientValue):
    deleted: Incomplete
    remaining: Incomplete
    state: Incomplete
    def __init__(self, deleted: Incomplete | None = None, remaining: Incomplete | None = None, state: Incomplete | None = None) -> None: ...
