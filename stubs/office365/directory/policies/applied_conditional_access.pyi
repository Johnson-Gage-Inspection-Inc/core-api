from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue
from office365.runtime.types.collections import StringCollection as StringCollection

class AppliedConditionalAccessPolicy(ClientValue):
    displayName: Incomplete
    enforcedGrantControls: Incomplete
    enforcedSessionControls: Incomplete
    id: Incomplete
    result: Incomplete
    def __init__(self, display_name: Incomplete | None = None, enforced_grant_controls: Incomplete | None = None, enforced_session_controls: Incomplete | None = None, id_: Incomplete | None = None, result: Incomplete | None = None) -> None: ...
