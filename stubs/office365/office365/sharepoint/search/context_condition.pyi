from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class ContextCondition(ClientValue):
    ContextConditionType: Incomplete
    SourceId: Incomplete
    def __init__(
        self,
        context_condition_type: Incomplete | None = None,
        source_id: Incomplete | None = None,
    ) -> None: ...
    @property
    def entity_type_name(self): ...
