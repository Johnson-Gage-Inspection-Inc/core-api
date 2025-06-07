from _typeshed import Incomplete
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath
from office365.sharepoint.entity import Entity as Entity
from office365.sharepoint.permissions.base_permissions import BasePermissions as BasePermissions
from office365.sharepoint.translation.user_resource import UserResource as UserResource

class UserCustomAction(Entity):
    def get_property(self, name, default_value: Incomplete | None = None): ...
    @property
    def rights(self): ...
    @property
    def description_resource(self): ...
    @property
    def title_resource(self): ...
