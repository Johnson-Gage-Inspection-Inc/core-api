from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class SearchObjectOwnerResult(ClientValue):
    SiteCollectionId: Incomplete
    SiteId: Incomplete
    TenantId: Incomplete
    def __init__(self, site_collection_id: Incomplete | None = None, site_id: Incomplete | None = None, tenant_id: Incomplete | None = None) -> None: ...
    @property
    def entity_type_name(self): ...
