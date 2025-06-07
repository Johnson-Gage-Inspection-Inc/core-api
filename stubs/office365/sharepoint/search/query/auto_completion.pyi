from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue
from office365.runtime.client_value_collection import ClientValueCollection as ClientValueCollection
from office365.sharepoint.search.query.auto_completion_match import QueryAutoCompletionMatch as QueryAutoCompletionMatch

class QueryAutoCompletion(ClientValue):
    Matches: Incomplete
    Query: Incomplete
    Score: Incomplete
    Source: Incomplete
    def __init__(self, query: Incomplete | None = None, score: Incomplete | None = None, source: Incomplete | None = None) -> None: ...
    @property
    def entity_type_name(self): ...
