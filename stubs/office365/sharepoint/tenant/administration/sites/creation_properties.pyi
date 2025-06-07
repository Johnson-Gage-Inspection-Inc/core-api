from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class SiteCreationProperties(ClientValue):
    Url: Incomplete
    Owner: Incomplete
    OwnerName: Incomplete
    Title: Incomplete
    Template: Incomplete
    SiteUniName: Incomplete
    def __init__(self, title: Incomplete | None = None, url: Incomplete | None = None, owner: Incomplete | None = None, owner_name: Incomplete | None = None, template: Incomplete | None = None, site_uni_name: Incomplete | None = None) -> None: ...
    @property
    def entity_type_name(self): ...
