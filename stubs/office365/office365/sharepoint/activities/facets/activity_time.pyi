from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class ActivityTimeFacet(ClientValue):
    lastRecordedTime: Incomplete
    observedTime: Incomplete
    recordedTime: Incomplete
    def __init__(
        self,
        last_recorded_time: Incomplete | None = None,
        observed_time: Incomplete | None = None,
        recorded_time: Incomplete | None = None,
    ) -> None: ...
