from _typeshed import Incomplete
from office365.outlook.calendar.email_address import EmailAddress as EmailAddress
from office365.runtime.client_value import ClientValue as ClientValue

class Recipient(ClientValue):
    emailAddress: Incomplete
    def __init__(self, email_address: Incomplete | None = None) -> None: ...
    @staticmethod
    def from_email(value): ...
