from _typeshed import Incomplete
from office365.delta_collection import DeltaCollection as DeltaCollection
from office365.outlook.calendar.attendees.attendee import Attendee as Attendee
from office365.outlook.calendar.dateTimeTimeZone import DateTimeTimeZone as DateTimeTimeZone
from office365.outlook.calendar.email_address import EmailAddress as EmailAddress
from office365.outlook.calendar.events.event import Event as Event
from office365.outlook.mail.item_body import ItemBody as ItemBody
from office365.runtime.client_value_collection import ClientValueCollection as ClientValueCollection

class EventCollection(DeltaCollection[Event]):
    def __init__(self, context, resource_path: Incomplete | None = None) -> None: ...
    def add(self, subject: Incomplete | None = None, body: Incomplete | None = None, start: Incomplete | None = None, end: Incomplete | None = None, attendees: Incomplete | None = None, **kwargs): ...
