from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue
from office365.runtime.client_value_collection import (
    ClientValueCollection as ClientValueCollection,
)
from office365.runtime.odata.type import ODataType as ODataType
from office365.runtime.types.collections import StringCollection as StringCollection
from office365.sharepoint.search.query_result import QueryResult as QueryResult

class SearchResult(ClientValue):
    PrimaryQueryResult: Incomplete
    ElapsedTime: Incomplete
    Properties: Incomplete
    SecondaryQueryResults: Incomplete
    SpellingSuggestion: Incomplete
    TriggeredRules: Incomplete
    def __init__(
        self,
        elapsed_time: Incomplete | None = None,
        primary_query_result=...,
        properties: Incomplete | None = None,
        secondary_query_results: Incomplete | None = None,
        spelling_suggestion: Incomplete | None = None,
        triggered_rules: Incomplete | None = None,
    ) -> None: ...
    def set_property(self, k, v, persist_changes: bool = True): ...
    @property
    def entity_type_name(self): ...
