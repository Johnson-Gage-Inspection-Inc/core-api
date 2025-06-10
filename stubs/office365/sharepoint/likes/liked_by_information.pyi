from _typeshed import Incomplete
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath
from office365.sharepoint.entity import Entity as Entity
from office365.sharepoint.entity_collection import EntityCollection as EntityCollection
from office365.sharepoint.likes.user_entity import UserEntity as UserEntity

class LikedByInformation(Entity):
    @property
    def like_count(self) -> int | None: ...
    @property
    def is_liked_by_user(self) -> bool | None: ...
    @property
    def liked_by(self) -> EntityCollection[UserEntity]: ...
    def get_property(self, name, default_value: Incomplete | None = None): ...
