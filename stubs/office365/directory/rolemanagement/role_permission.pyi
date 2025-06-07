from _typeshed import Incomplete
from office365.directory.rolemanagement.resource_action import ResourceAction as ResourceAction
from office365.runtime.client_value import ClientValue as ClientValue
from office365.runtime.client_value_collection import ClientValueCollection as ClientValueCollection

class RolePermission(ClientValue):
    resourceActions: Incomplete
    def __init__(self, resource_actions: Incomplete | None = None) -> None: ...
