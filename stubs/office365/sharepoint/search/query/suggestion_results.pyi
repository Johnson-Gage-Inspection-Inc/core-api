from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue
from office365.runtime.client_value_collection import ClientValueCollection as ClientValueCollection
from office365.runtime.types.collections import StringCollection as StringCollection
from office365.sharepoint.search.query.personal_result_suggestion import PersonalResultSuggestion as PersonalResultSuggestion

class QuerySuggestionQuery(ClientValue):
    @property
    def entity_type_name(self): ...

class QuerySuggestionResults(ClientValue):
    PeopleNames: Incomplete
    PersonalResults: Incomplete
    PopularResults: Incomplete
    Queries: Incomplete
    def __init__(self, people_names: Incomplete | None = None) -> None: ...
    @property
    def entity_type_name(self): ...
