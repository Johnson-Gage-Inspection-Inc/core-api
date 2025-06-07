from _typeshed import Incomplete
from office365.directory.protection.riskyusers.risky_user import RiskyUser as RiskyUser
from office365.entity_collection import EntityCollection as EntityCollection
from office365.runtime.queries.service_operation import (
    ServiceOperationQuery as ServiceOperationQuery,
)
from office365.runtime.types.collections import StringCollection as StringCollection

class RiskyUserCollection(EntityCollection[RiskyUser]):
    def __init__(self, context, resource_path: Incomplete | None = None) -> None: ...
    def confirm_compromised(self, user_ids: Incomplete | None = None): ...
    def dismiss(self, user_ids: Incomplete | None = None): ...
