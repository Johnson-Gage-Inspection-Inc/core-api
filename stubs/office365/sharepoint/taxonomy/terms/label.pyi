from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class Label(ClientValue):
    name: Incomplete
    isDefault: Incomplete
    languageTag: Incomplete
    def __init__(
        self,
        name: Incomplete | None = None,
        is_default: Incomplete | None = None,
        language_tag: Incomplete | None = None,
    ) -> None: ...
