from _typeshed import Incomplete
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath
from office365.runtime.queries.service_operation import ServiceOperationQuery as ServiceOperationQuery
from office365.sharepoint.entity import Entity as Entity

class SPAnalyticsUsageService(Entity):
    def __init__(self, context) -> None: ...
    def log_event(self, event_type_id, scope_id, item_id, site: Incomplete | None = None, user: Incomplete | None = None): ...
    @property
    def entity_type_name(self): ...
