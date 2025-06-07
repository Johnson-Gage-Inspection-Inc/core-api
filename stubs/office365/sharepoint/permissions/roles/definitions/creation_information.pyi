from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue
from office365.sharepoint.permissions.base_permissions import BasePermissions as BasePermissions

class RoleDefinitionCreationInformation(ClientValue):
    Name: Incomplete
    Description: Incomplete
    BasePermissions: Incomplete
    Order: Incomplete
    def __init__(self, base_permissions=..., name: Incomplete | None = None, description: Incomplete | None = None, order: Incomplete | None = None) -> None: ...
    @property
    def entity_type_name(self): ...
