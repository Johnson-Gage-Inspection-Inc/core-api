from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue
from office365.runtime.client_value_collection import (
    ClientValueCollection as ClientValueCollection,
)
from office365.sharepoint.marketplace.corporatecuratedgallery.addins.instance_info import (
    SPAddinInstanceInfo as SPAddinInstanceInfo,
)

class SPAvailableAddinsResponse(ClientValue):
    addins: Incomplete
    def __init__(self, addins: Incomplete | None = None) -> None: ...
    @property
    def entity_type_name(self): ...
