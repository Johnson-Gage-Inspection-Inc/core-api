from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue
from office365.runtime.client_value_collection import ClientValueCollection as ClientValueCollection
from office365.sharepoint.sharing.links.default_template import SharingLinkDefaultTemplate as SharingLinkDefaultTemplate

class SharingLinkDefaultTemplatesCollection(ClientValue):
    templates: Incomplete
    def __init__(self, templates: Incomplete | None = None) -> None: ...
