from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue
from office365.runtime.client_value_collection import (
    ClientValueCollection as ClientValueCollection,
)
from office365.sharepoint.lists.currency_information import (
    CurrencyInformation as CurrencyInformation,
)

class CurrencyInformationCollection(ClientValue):
    Items: Incomplete
    def __init__(self, items: Incomplete | None = None) -> None: ...
