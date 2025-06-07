from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class LocaleInfo(ClientValue):
    displayName: Incomplete
    locale: Incomplete
    def __init__(
        self, display_name: Incomplete | None = None, locale: Incomplete | None = None
    ) -> None: ...
