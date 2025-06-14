from _typeshed import Incomplete
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath
from office365.sharepoint.entity import Entity as Entity
from office365.sharepoint.permissions.roles.definitions.collection import (
    RoleDefinitionCollection as RoleDefinitionCollection,
)
from office365.sharepoint.principal.principal import Principal as Principal

class RoleAssignment(Entity):
    @property
    def principal_id(self): ...
    @property
    def member(self): ...
    @property
    def role_definition_bindings(self): ...
    def get_property(self, name, default_value: Incomplete | None = None): ...
    def set_property(self, name, value, persist_changes: bool = True): ...
