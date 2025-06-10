from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue
from office365.runtime.types.collections import StringCollection as StringCollection

class GroupProfile(ClientValue):
    mailNickname: Incomplete
    displayName: Incomplete
    description: Incomplete
    mailEnabled: Incomplete
    securityEnabled: Incomplete
    owners: Incomplete
    members: Incomplete
    groupTypes: Incomplete
    def __init__(
        self,
        name,
        description: Incomplete | None = None,
        mail_enabled: bool = False,
        security_enabled: bool = True,
        group_types: Incomplete | None = None,
    ) -> None: ...
