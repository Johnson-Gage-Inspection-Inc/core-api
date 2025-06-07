from _typeshed import Incomplete
from office365.delta_collection import DeltaCollection as DeltaCollection
from office365.directory.users.user import User as User
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath
from office365.runtime.queries.create_entity import CreateEntityQuery as CreateEntityQuery

class UserCollection(DeltaCollection[User]):
    def __init__(self, context, resource_path: Incomplete | None = None) -> None: ...
    def get_by_principal_name(self, name): ...
    def add(self, user_properties): ...
