from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class LicenseUnitsDetail(ClientValue):
    enabled: Incomplete
    lockedOut: Incomplete
    suspended: Incomplete
    warning: Incomplete
    def __init__(
        self,
        enabled: Incomplete | None = None,
        locked_out: Incomplete | None = None,
        suspended: Incomplete | None = None,
        warning: Incomplete | None = None,
    ) -> None: ...
