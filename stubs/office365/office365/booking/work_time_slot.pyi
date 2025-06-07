from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class BookingWorkTimeSlot(ClientValue):
    endTime: Incomplete
    startTime: Incomplete
    def __init__(
        self, end_time: Incomplete | None = None, start_time: Incomplete | None = None
    ) -> None: ...
