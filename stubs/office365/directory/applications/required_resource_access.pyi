from _typeshed import Incomplete
from office365.directory.applications.resource_access import ResourceAccess as ResourceAccess
from office365.runtime.client_value import ClientValue as ClientValue
from office365.runtime.client_value_collection import ClientValueCollection as ClientValueCollection

class RequiredResourceAccess(ClientValue):
    resourceAccess: Incomplete
    resourceAppId: Incomplete
    def __init__(self, resource_access: Incomplete | None = None, resource_app_id: Incomplete | None = None) -> None: ...
