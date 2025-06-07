from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class IdleSessionSignOut(ClientValue):
    isEnabled: Incomplete
    signOutAfterInSeconds: Incomplete
    warnAfterInSeconds: Incomplete
    def __init__(self, is_enabled: Incomplete | None = None, sign_out_after_in_seconds: Incomplete | None = None, warn_after_in_seconds: Incomplete | None = None) -> None: ...
