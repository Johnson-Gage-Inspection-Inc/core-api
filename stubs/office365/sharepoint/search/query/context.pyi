from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue
from office365.runtime.types.collections import StringCollection as StringCollection

class QueryContext(ClientValue):
    GroupObjectIds: Incomplete
    SpSiteId: Incomplete
    TenantInstanceId: Incomplete
    def __init__(self, group_object_ids: Incomplete | None = None, site_id: Incomplete | None = None, tenant_instance_id: Incomplete | None = None) -> None: ...
    @property
    def entity_type_name(self): ...
