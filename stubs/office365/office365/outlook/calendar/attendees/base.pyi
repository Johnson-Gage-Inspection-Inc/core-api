from _typeshed import Incomplete
from office365.outlook.mail.recipient import Recipient as Recipient

class AttendeeBase(Recipient):
    type: Incomplete
    def __init__(
        self,
        email_address: Incomplete | None = None,
        attendee_type: Incomplete | None = None,
    ) -> None: ...
