from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue
from office365.teams.apps.permission_set import (
    TeamsAppPermissionSet as TeamsAppPermissionSet,
)

class TeamsAppAuthorization(ClientValue):
    clientAppId: Incomplete
    requiredPermissionSet: Incomplete
    def __init__(
        self, client_app_id: Incomplete | None = None, required_permission_set=...
    ) -> None: ...
