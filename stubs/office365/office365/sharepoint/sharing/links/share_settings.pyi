from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class ShareLinkSettings(ClientValue):
    allowAnonymousAccess: Incomplete
    applicationLink: Incomplete
    linkKind: Incomplete
    expiration: Incomplete
    password: Incomplete
    passwordProtected: Incomplete
    role: Incomplete
    shareId: Incomplete
    trackLinkUsers: Incomplete
    updatePassword: Incomplete
    def __init__(
        self,
        allow_anonymous_access: Incomplete | None = None,
        application_link: Incomplete | None = None,
        link_kind: Incomplete | None = None,
        expiration: Incomplete | None = None,
        password: Incomplete | None = None,
        password_protected: Incomplete | None = None,
        role: Incomplete | None = None,
        track_link_users: Incomplete | None = None,
        share_id: Incomplete | None = None,
        update_password: Incomplete | None = None,
    ) -> None: ...
    @property
    def entity_type_name(self): ...
