from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue
from office365.runtime.client_value_collection import ClientValueCollection as ClientValueCollection
from office365.sharepoint.portal.linkedsites.contract import LinkedSiteContract as LinkedSiteContract

class LinkedSitesListContract(ClientValue):
    LinkedSites: Incomplete
    def __init__(self, linked_sites=...) -> None: ...
    @property
    def entity_type_name(self): ...
