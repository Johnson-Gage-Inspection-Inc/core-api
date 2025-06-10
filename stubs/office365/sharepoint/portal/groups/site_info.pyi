from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class GroupSiteInfo(ClientValue):
    SiteStatus: Incomplete
    SiteUrl: Incomplete
    DocumentsUrl: Incomplete
    ErrorMessage: Incomplete
    GroupId: Incomplete
    def __init__(
        self, site_url: Incomplete | None = None, site_status: Incomplete | None = None
    ) -> None: ...
