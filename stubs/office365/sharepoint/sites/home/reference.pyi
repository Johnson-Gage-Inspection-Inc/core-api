from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class SPHSiteReference(ClientValue):
    LogoUrl: Incomplete
    Title: Incomplete
    Url: Incomplete
    def __init__(self, logo_url: Incomplete | None = None, title: Incomplete | None = None, url: Incomplete | None = None) -> None: ...
    @property
    def entity_type_name(self): ...
