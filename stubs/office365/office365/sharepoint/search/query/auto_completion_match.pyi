from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class QueryAutoCompletionMatch(ClientValue):
    Alternation: Incomplete
    Key: Incomplete
    def __init__(
        self, alternation: Incomplete | None = None, key: Incomplete | None = None
    ) -> None: ...
    @property
    def entity_type_name(self): ...
