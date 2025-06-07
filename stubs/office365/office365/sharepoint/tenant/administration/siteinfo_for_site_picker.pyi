from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class SiteInfoForSitePicker(ClientValue):
    Error: Incomplete
    SiteId: Incomplete
    SiteName: Incomplete
    Url: Incomplete
    def __init__(
        self,
        Error: str = None,
        site_id: str = None,
        site_name: str = None,
        Url: str = None,
    ) -> None: ...
    @property
    def entity_type_name(self): ...
