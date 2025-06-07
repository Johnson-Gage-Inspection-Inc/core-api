from _typeshed import Incomplete
from office365.outlook.calendar.attendees.base import AttendeeBase as AttendeeBase
from office365.runtime.client_value import ClientValue as ClientValue

class AttendeeAvailability(ClientValue):
    attendee: Incomplete
    availability: Incomplete
    def __init__(self, attendee=..., availability: Incomplete | None = None) -> None: ...
