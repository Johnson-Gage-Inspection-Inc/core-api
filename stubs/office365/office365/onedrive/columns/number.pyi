from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class NumberColumn(ClientValue):
    minimum: Incomplete
    maximum: Incomplete
    displayAs: Incomplete
    decimalPlaces: Incomplete
    def __init__(
        self,
        minimum: Incomplete | None = None,
        maximum: Incomplete | None = None,
        display_as: Incomplete | None = None,
        decimal_places: Incomplete | None = None,
    ) -> None: ...
