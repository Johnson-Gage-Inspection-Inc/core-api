from _typeshed import Incomplete
from office365.booking.work_time_slot import BookingWorkTimeSlot as BookingWorkTimeSlot
from office365.runtime.client_value import ClientValue as ClientValue
from office365.runtime.client_value_collection import (
    ClientValueCollection as ClientValueCollection,
)

class BookingWorkHours(ClientValue):
    day: Incomplete
    timeSlots: Incomplete
    def __init__(
        self, day: Incomplete | None = None, time_slots: Incomplete | None = None
    ) -> None: ...
