from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class VivaSiteRequestInfo(ClientValue):
    IsAlreadyAdded: Incomplete
    SiteUrl: Incomplete
    def __init__(
        self,
        is_already_added: Incomplete | None = None,
        site_url: Incomplete | None = None,
    ) -> None: ...
    @property
    def entity_type_name(self): ...
