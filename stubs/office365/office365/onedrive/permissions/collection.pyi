from _typeshed import Incomplete
from office365.directory.applications.application import Application as Application
from office365.directory.groups.group import Group as Group
from office365.directory.permissions.identity import Identity as Identity
from office365.directory.users.user import User as User
from office365.entity import Entity as Entity
from office365.entity_collection import EntityCollection as EntityCollection
from office365.intune.devices.device import Device as Device
from office365.onedrive.permissions.permission import Permission as Permission
from office365.runtime.queries.create_entity import (
    CreateEntityQuery as CreateEntityQuery,
)

class PermissionCollection(EntityCollection[Permission]):
    def __init__(self, context, resource_path: Incomplete | None = None) -> None: ...
    def add(
        self,
        roles: list[str],
        identity: Application | User | Group | Device | str = None,
        identity_type: str = None,
    ) -> Permission: ...
    def delete_all(self): ...
