from _typeshed import Incomplete
from office365.outlook.calendar.timezones.base import TimeZoneBase as TimeZoneBase

class CustomTimeZone(TimeZoneBase):
    bias: Incomplete
    def __init__(self, bias: Incomplete | None = None) -> None: ...
