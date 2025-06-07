from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class PlannerPlanContainer(ClientValue):
    containerId: Incomplete
    type: Incomplete
    url: Incomplete
    def __init__(
        self,
        container_id: Incomplete | None = None,
        type_: Incomplete | None = None,
        url: Incomplete | None = None,
    ) -> None: ...
