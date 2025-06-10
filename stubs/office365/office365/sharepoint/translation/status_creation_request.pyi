from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue
from office365.runtime.types.collections import StringCollection as StringCollection

class TranslationStatusCreationRequest(ClientValue):
    LanguageCodes: Incomplete
    def __init__(self, language_codes: Incomplete | None = None) -> None: ...
