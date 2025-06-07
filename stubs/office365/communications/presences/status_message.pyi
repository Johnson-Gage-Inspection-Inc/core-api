from _typeshed import Incomplete
from office365.outlook.calendar.dateTimeTimeZone import DateTimeTimeZone as DateTimeTimeZone
from office365.outlook.mail.item_body import ItemBody as ItemBody
from office365.runtime.client_value import ClientValue as ClientValue

class PresenceStatusMessage(ClientValue):
    expiryDateTime: Incomplete
    message: Incomplete
    publishedDateTime: Incomplete
    def __init__(self, expiry_datetime=..., message=..., published_datetime: Incomplete | None = None) -> None: ...
