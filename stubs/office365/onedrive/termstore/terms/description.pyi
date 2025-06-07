from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class LocalizedDescription(ClientValue):
    languageTag: Incomplete
    description: Incomplete
    def __init__(self, language_tag: Incomplete | None = None, description: Incomplete | None = None) -> None: ...
