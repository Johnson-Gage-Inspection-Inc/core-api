from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class DisplayNameLocalization(ClientValue):
    displayName: Incomplete
    languageTag: Incomplete
    def __init__(
        self,
        display_name: Incomplete | None = None,
        language_tag: Incomplete | None = None,
    ) -> None: ...
