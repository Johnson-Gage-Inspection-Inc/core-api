from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class LocalizedName(ClientValue):
    name: Incomplete
    languageTag: Incomplete
    def __init__(self, name: Incomplete | None = None, language_tag: str = 'en-US') -> None: ...
