from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class AssignedPlan(ClientValue):
    assignedDateTime: Incomplete
    capabilityStatus: Incomplete
    service: Incomplete
    servicePlanId: Incomplete
    def __init__(
        self,
        assigned_datetime: Incomplete | None = None,
        capability_status: Incomplete | None = None,
        service: Incomplete | None = None,
        service_plan_id: Incomplete | None = None,
    ) -> None: ...
