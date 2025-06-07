from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue
from office365.runtime.client_value_collection import ClientValueCollection as ClientValueCollection
from office365.teams.apps.resource_specific_permission import TeamsAppResourceSpecificPermission as TeamsAppResourceSpecificPermission

class TeamsAppPermissionSet(ClientValue):
    resourceSpecificPermissions: Incomplete
    def __init__(self, resource_specific_permissions: Incomplete | None = None) -> None: ...
