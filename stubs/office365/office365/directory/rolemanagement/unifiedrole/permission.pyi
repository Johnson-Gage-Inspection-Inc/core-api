from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue
from office365.runtime.types.collections import StringCollection as StringCollection

class UnifiedRolePermission(ClientValue):
    allowedResourceActions: Incomplete
    condition: Incomplete
    excludedResourceActions: Incomplete
    def __init__(
        self,
        allowed_resource_actions: Incomplete | None = None,
        condition: Incomplete | None = None,
        excluded_resource_actions: Incomplete | None = None,
    ) -> None: ...
