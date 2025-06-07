from _typeshed import Incomplete
from office365.outlook.calendar.attendees.base import AttendeeBase as AttendeeBase
from office365.outlook.calendar.email_address import EmailAddress as EmailAddress

class Attendee(AttendeeBase):
    proposedNewTime: Incomplete
    status: Incomplete
    def __init__(self, email_address=..., attendee_type: Incomplete | None = None, proposed_new_time: Incomplete | None = None, status: Incomplete | None = None) -> None: ...
