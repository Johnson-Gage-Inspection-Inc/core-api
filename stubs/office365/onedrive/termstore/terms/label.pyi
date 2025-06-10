from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class LocalizedLabel(ClientValue):
    name: Incomplete
    languageTag: Incomplete
    isDefault: Incomplete
    def __init__(
        self,
        name: Incomplete | None = None,
        language_tag: str = "en-US",
        is_default: bool = True,
    ) -> None: ...
