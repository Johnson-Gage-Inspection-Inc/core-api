from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class PersonalResultSuggestion(ClientValue):
    HighlightedTitle: Incomplete
    IsBestBet: Incomplete
    Title: Incomplete
    Url: Incomplete
    def __init__(self, highlighted_title: Incomplete | None = None, is_best_bet: Incomplete | None = None, title: Incomplete | None = None, url: Incomplete | None = None) -> None: ...
    @property
    def entity_type_name(self): ...
