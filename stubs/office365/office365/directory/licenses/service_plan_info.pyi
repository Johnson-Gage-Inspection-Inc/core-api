from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class ServicePlanInfo(ClientValue):
    servicePlanId: Incomplete
    servicePlanName: Incomplete
    provisioningStatus: Incomplete
    appliesTo: Incomplete
    def __init__(
        self,
        _id: Incomplete | None = None,
        name: Incomplete | None = None,
        provisioning_status: Incomplete | None = None,
        applies_to: Incomplete | None = None,
    ) -> None: ...
