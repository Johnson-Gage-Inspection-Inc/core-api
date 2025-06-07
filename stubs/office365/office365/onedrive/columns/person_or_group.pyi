from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class PersonOrGroupColumn(ClientValue):
    allowMultipleSelection: Incomplete
    chooseFromType: Incomplete
    displayAs: Incomplete
    def __init__(
        self,
        allow_multiple_selection: Incomplete | None = None,
        choose_from_type: Incomplete | None = None,
        display_as: Incomplete | None = None,
    ) -> None: ...
