from _typeshed import Incomplete
from office365.outlook.mail.patterned_recurrence import PatternedRecurrence as PatternedRecurrence
from office365.runtime.client_value import ClientValue as ClientValue
from office365.runtime.client_value_collection import ClientValueCollection as ClientValueCollection
from office365.teams.schedule.shifts.time_range import TimeRange as TimeRange

class ShiftAvailability(ClientValue):
    recurrence: Incomplete
    timeSlots: Incomplete
    timeZone: Incomplete
    def __init__(self, recurrence=..., time_slots: Incomplete | None = None, time_zone: Incomplete | None = None) -> None: ...
