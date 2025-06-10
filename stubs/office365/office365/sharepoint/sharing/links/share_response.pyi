from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue
from office365.sharepoint.sharing.links.info import SharingLinkInfo as SharingLinkInfo

class ShareLinkResponse(ClientValue):
    sharingLinkInfo: Incomplete
    def __init__(self, sharing_link_info=...) -> None: ...
    @property
    def entity_type_name(self): ...
