from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue
from office365.runtime.types.collections import StringCollection as StringCollection

class AppRole(ClientValue):
    id: Incomplete
    allowedMemberTypes: Incomplete
    description: Incomplete
    displayName: Incomplete
    isEnabled: Incomplete
    origin: Incomplete
    value: Incomplete
    def __init__(self, id_: Incomplete | None = None, allowed_member_types: Incomplete | None = None, description: Incomplete | None = None, display_name: Incomplete | None = None, is_enabled: Incomplete | None = None, origin: Incomplete | None = None, value: Incomplete | None = None) -> None: ...
