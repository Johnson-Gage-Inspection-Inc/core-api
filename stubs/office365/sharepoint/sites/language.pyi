from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class Language(ClientValue):
    DisplayName: Incomplete
    LanguageTag: Incomplete
    Lcid: Incomplete
    def __init__(self, display_name: Incomplete | None = None, language_tag: Incomplete | None = None, lcid: Incomplete | None = None) -> None: ...
