from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue
from office365.runtime.client_value_collection import (
    ClientValueCollection as ClientValueCollection,
)
from office365.sharepoint.translation.requested_translation import (
    RequestedTranslation as RequestedTranslation,
)

class TranslationStatusSetRequest(ClientValue):
    RequestedTranslations: Incomplete
    def __init__(self, values: Incomplete | None = None) -> None: ...
