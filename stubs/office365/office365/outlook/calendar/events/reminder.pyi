from _typeshed import Incomplete
from office365.outlook.calendar.dateTimeTimeZone import (
    DateTimeTimeZone as DateTimeTimeZone,
)
from office365.outlook.mail.location import Location as Location
from office365.runtime.client_value import ClientValue as ClientValue

class Reminder(ClientValue):
    changeKey: Incomplete
    eventStartTime: Incomplete
    eventEndTime: Incomplete
    eventId: Incomplete
    eventLocation: Incomplete
    eventSubject: Incomplete
    eventWebLink: Incomplete
    reminderFireTime: Incomplete
    def __init__(
        self,
        change_key: Incomplete | None = None,
        event_end_time=...,
        event_id: Incomplete | None = None,
        event_location=...,
        event_start_time=...,
        event_subject: Incomplete | None = None,
        event_web_link: Incomplete | None = None,
        reminder_fire_time=...,
    ) -> None: ...
