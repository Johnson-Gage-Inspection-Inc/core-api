from _typeshed import Incomplete
from office365.outlook.calendar.meetingtimes.time_slot import TimeSlot as TimeSlot
from office365.runtime.client_value import ClientValue as ClientValue
from office365.runtime.client_value_collection import ClientValueCollection as ClientValueCollection

class TimeConstraint(ClientValue):
    activityDomain: Incomplete
    timeSlots: Incomplete
    def __init__(self, activity_domain: Incomplete | None = None, time_slots: Incomplete | None = None) -> None: ...
