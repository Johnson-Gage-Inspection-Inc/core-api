from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue
from office365.runtime.client_value_collection import (
    ClientValueCollection as ClientValueCollection,
)
from office365.runtime.odata.type import ODataType as ODataType
from office365.sharepoint.sharing.role import Role as Role

class UserSharingResult(ClientValue):
    AllowedRoles: Incomplete
    CurrentRole: Incomplete
    DisplayName: Incomplete
    Email: Incomplete
    InvitationLink: Incomplete
    IsUserKnown: Incomplete
    Message: Incomplete
    Status: Incomplete
    User: Incomplete
    def __init__(
        self,
        allowed_roles: Incomplete | None = None,
        current_role: Incomplete | None = None,
        display_name: Incomplete | None = None,
        email: Incomplete | None = None,
        invitation_link: Incomplete | None = None,
        is_user_known: Incomplete | None = None,
        message: Incomplete | None = None,
        status: Incomplete | None = None,
        user: Incomplete | None = None,
    ) -> None: ...
    @property
    def current_role_name(self): ...
    @property
    def entity_type_name(self): ...
