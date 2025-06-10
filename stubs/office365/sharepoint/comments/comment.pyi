from _typeshed import Incomplete
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath
from office365.runtime.queries.service_operation import (
    ServiceOperationQuery as ServiceOperationQuery,
)
from office365.sharepoint.entity import Entity as Entity
from office365.sharepoint.entity_collection import EntityCollection as EntityCollection
from office365.sharepoint.likes.user_entity import UserEntity as UserEntity

class Comment(Entity):
    def like(self): ...
    def unlike(self): ...
    @property
    def liked_by(self): ...
    @property
    def entity_type_name(self): ...
    def get_property(self, name, default_value: Incomplete | None = None): ...
