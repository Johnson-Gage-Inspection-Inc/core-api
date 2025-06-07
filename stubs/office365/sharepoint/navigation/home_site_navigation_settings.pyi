from _typeshed import Incomplete
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath
from office365.runtime.queries.service_operation import ServiceOperationQuery as ServiceOperationQuery
from office365.sharepoint.entity import Entity as Entity

class HomeSiteNavigationSettings(Entity):
    def __init__(self, context, resource_path: Incomplete | None = None) -> None: ...
    def enable_global_navigation(self, is_enabled): ...
    @property
    def entity_type_name(self): ...
