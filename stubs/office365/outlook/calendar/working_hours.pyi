from _typeshed import Incomplete
from office365.outlook.calendar.timezones.base import TimeZoneBase as TimeZoneBase
from office365.runtime.client_value import ClientValue as ClientValue
from office365.runtime.types.collections import StringCollection as StringCollection

class WorkingHours(ClientValue):
    daysOfWeek: Incomplete
    timeZone: Incomplete
    endTime: Incomplete
    startTime: Incomplete
    def __init__(self, days_of_week: Incomplete | None = None, end_time: Incomplete | None = None, start_time: Incomplete | None = None, timezone=...) -> None: ...
