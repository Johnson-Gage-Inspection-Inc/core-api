from _typeshed import Incomplete
from office365.directory.permissions.scope import PermissionScope as PermissionScope
from office365.runtime.client_value import ClientValue as ClientValue
from office365.runtime.client_value_collection import (
    ClientValueCollection as ClientValueCollection,
)
from office365.runtime.types.collections import StringCollection as StringCollection

class ApiApplication(ClientValue):
    acceptMappedClaims: Incomplete
    knownClientApplications: Incomplete
    oauth2PermissionScopes: Incomplete
    def __init__(
        self,
        accept_mapped_claims: Incomplete | None = None,
        known_client_applications: Incomplete | None = None,
        oauth2_permission_scopes: Incomplete | None = None,
    ) -> None: ...
