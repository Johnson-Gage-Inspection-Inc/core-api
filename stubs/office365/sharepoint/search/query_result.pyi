from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue
from office365.runtime.client_value_collection import ClientValueCollection as ClientValueCollection
from office365.sharepoint.search.custom_result import CustomResult as CustomResult
from office365.sharepoint.search.refinement_results import RefinementResults as RefinementResults
from office365.sharepoint.search.relevant_results import RelevantResults as RelevantResults
from office365.sharepoint.search.special_term_results import SpecialTermResults as SpecialTermResults

class QueryResult(ClientValue):
    QueryId: Incomplete
    QueryRuleId: Incomplete
    RefinementResults: Incomplete
    CustomResults: Incomplete
    RelevantResults: Incomplete
    SpecialTermResults: Incomplete
    def __init__(self, query_id: Incomplete | None = None, custom_results: Incomplete | None = None, refinement_results=..., relevant_results=..., query_rule_id: Incomplete | None = None, special_term_results=...) -> None: ...
    @property
    def entity_type_name(self): ...
