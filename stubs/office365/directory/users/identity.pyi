from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class UserIdentity(ClientValue):
    displayName: Incomplete
    ipAddress: Incomplete
    userPrincipalName: Incomplete
    def __init__(self, display_name: Incomplete | None = None, ip_address: Incomplete | None = None, user_principal_name: Incomplete | None = None) -> None: ...
