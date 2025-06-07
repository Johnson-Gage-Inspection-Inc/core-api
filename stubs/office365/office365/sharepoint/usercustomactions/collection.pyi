from _typeshed import Incomplete
from office365.runtime.queries.service_operation import (
    ServiceOperationQuery as ServiceOperationQuery,
)
from office365.sharepoint.entity_collection import EntityCollection as EntityCollection
from office365.sharepoint.usercustomactions.action import (
    UserCustomAction as UserCustomAction,
)

class UserCustomActionCollection(EntityCollection[UserCustomAction]):
    def __init__(self, context, resource_path: Incomplete | None = None) -> None: ...
    def clear(self): ...
