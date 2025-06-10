from _typeshed import Incomplete
from office365.directory.users.activities.activity import UserActivity as UserActivity
from office365.entity_collection import EntityCollection as EntityCollection
from office365.runtime.queries.function import FunctionQuery as FunctionQuery

class UserActivityCollection(EntityCollection[UserActivity]):
    def __init__(self, context, resource_path: Incomplete | None = None) -> None: ...
    def recent(self): ...
