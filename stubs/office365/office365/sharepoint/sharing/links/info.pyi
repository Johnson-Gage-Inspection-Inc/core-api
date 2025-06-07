from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue
from office365.runtime.client_value_collection import (
    ClientValueCollection as ClientValueCollection,
)
from office365.sharepoint.sharing.invitation.link import (
    LinkInvitation as LinkInvitation,
)
from office365.sharepoint.sharing.principal import Principal as Principal

class SharingLinkInfo(ClientValue):
    AllowsAnonymousAccess: Incomplete
    ApplicationId: Incomplete
    Created: Incomplete
    CreatedBy: Incomplete
    PasswordProtected: Incomplete
    Invitations: Incomplete
    RedeemedUsers: Incomplete
    LastModifiedBy: Incomplete
    PasswordLastModifiedBy: Incomplete
    TrackLinkUsers: Incomplete
    ShareTokenString: Incomplete
    Url: Incomplete
    def __init__(
        self,
        allows_anonymous_access: Incomplete | None = None,
        application_id: Incomplete | None = None,
        created: Incomplete | None = None,
        created_by=...,
        password_protected: Incomplete | None = None,
        invitations: Incomplete | None = None,
        redeemed_users: Incomplete | None = None,
        last_modified_by=...,
        password_last_modified_by=...,
        track_link_users: Incomplete | None = None,
        share_token_string: Incomplete | None = None,
        url: Incomplete | None = None,
    ) -> None: ...
    @property
    def entity_type_name(self): ...
