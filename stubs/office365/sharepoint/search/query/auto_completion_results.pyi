from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue
from office365.runtime.client_value_collection import ClientValueCollection as ClientValueCollection
from office365.sharepoint.search.query.auto_completion import QueryAutoCompletion as QueryAutoCompletion

class QueryAutoCompletionResults(ClientValue):
    CoreExecutionTimeMs: Incomplete
    CorrelationId: Incomplete
    Queries: Incomplete
    def __init__(self, core_execution_time_ms: Incomplete | None = None, correlation_id: Incomplete | None = None, queries: Incomplete | None = None) -> None: ...
    @property
    def entity_type_name(self): ...
