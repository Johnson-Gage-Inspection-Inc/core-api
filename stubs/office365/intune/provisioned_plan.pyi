from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class ProvisionedPlan(ClientValue):
    service: Incomplete
    provisioningStatus: Incomplete
    capabilityStatus: Incomplete
    def __init__(
        self,
        service: Incomplete | None = None,
        provisioning_status: Incomplete | None = None,
        capability_status: Incomplete | None = None,
    ) -> None: ...
