from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class SPSiteCreationResponse(ClientValue):
    SiteId: Incomplete
    SiteStatus: Incomplete
    SiteUrl: Incomplete
    def __init__(self) -> None: ...
    @property
    def entity_type_name(self): ...
