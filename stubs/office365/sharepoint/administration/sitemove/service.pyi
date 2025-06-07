from _typeshed import Incomplete
from office365.runtime.client_result import ClientResult as ClientResult
from office365.runtime.client_value import ClientValue as ClientValue
from office365.runtime.paths.service_operation import ServiceOperationPath as ServiceOperationPath
from office365.runtime.queries.service_operation import ServiceOperationQuery as ServiceOperationQuery
from office365.sharepoint.client_context import ClientContext as ClientContext
from office365.sharepoint.entity import Entity as Entity

class SystemSiteLockExpirationResult(ClientValue):
    Error: Incomplete
    Expiration: Incomplete
    def __init__(self, error: Incomplete | None = None, expiration: Incomplete | None = None) -> None: ...

class SiteMoveService(Entity):
    def __init__(self, context: ClientContext, site_id: str, site_subscription_id: str = None, source_database_id: str = None, target_database_id: str = None) -> None: ...
    def acquire_system_site_lock(self, lock_requestor, lock_type, lease_duration_in_minutes): ...
    @property
    def entity_type_name(self): ...
