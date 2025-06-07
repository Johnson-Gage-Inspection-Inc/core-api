from _typeshed import Incomplete
from office365.outlook.calendar.dateTimeTimeZone import DateTimeTimeZone as DateTimeTimeZone
from office365.runtime.client_value import ClientValue as ClientValue

class TimeSlot(ClientValue):
    start: Incomplete
    end: Incomplete
    def __init__(self, start=..., end=...) -> None: ...
