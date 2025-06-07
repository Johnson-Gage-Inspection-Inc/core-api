from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class SiteScriptActionResult(ClientValue):
    OutcomeText: Incomplete
    Target: Incomplete
    def __init__(self, outcome_text: Incomplete | None = None, target: Incomplete | None = None) -> None: ...
    @property
    def entity_type_name(self): ...
