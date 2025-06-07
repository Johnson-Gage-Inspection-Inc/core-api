from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class PermissionScope(ClientValue):
    adminConsentDescription: Incomplete
    adminConsentDisplayName: Incomplete
    id: Incomplete
    isEnabled: Incomplete
    origin: Incomplete
    type: Incomplete
    userConsentDescription: Incomplete
    userConsentDisplayName: Incomplete
    value: Incomplete
    def __init__(
        self,
        admin_consent_display_name: Incomplete | None = None,
        admin_consent_description: Incomplete | None = None,
        id_: Incomplete | None = None,
        is_enabled: Incomplete | None = None,
        origin: Incomplete | None = None,
        type_: Incomplete | None = None,
        user_consent_description: Incomplete | None = None,
        user_consent_display_name: Incomplete | None = None,
        value: Incomplete | None = None,
    ) -> None: ...
