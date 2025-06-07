from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue
from office365.runtime.client_value_collection import ClientValueCollection as ClientValueCollection
from office365.sharepoint.search.context_condition import ContextCondition as ContextCondition

class PromotedResultQueryRule(ClientValue):
    Contact: Incomplete
    ContextConditions: Incomplete
    CreationDate: Incomplete
    def __init__(self, contact: Incomplete | None = None, context_conditions: Incomplete | None = None, creation_date: Incomplete | None = None) -> None: ...
    @property
    def entity_type_name(self): ...
