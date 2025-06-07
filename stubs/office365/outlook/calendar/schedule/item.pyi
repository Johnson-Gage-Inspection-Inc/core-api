from _typeshed import Incomplete
from office365.outlook.calendar.dateTimeTimeZone import DateTimeTimeZone as DateTimeTimeZone
from office365.runtime.client_value import ClientValue as ClientValue

class ScheduleItem(ClientValue):
    start: Incomplete
    end: Incomplete
    location: Incomplete
    isPrivate: Incomplete
    subject: Incomplete
    status: Incomplete
    def __init__(self, start=..., end=..., location: Incomplete | None = None, is_private: Incomplete | None = None, subject: Incomplete | None = None, status: Incomplete | None = None) -> None: ...
