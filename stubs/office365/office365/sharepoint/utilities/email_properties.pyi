from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue
from office365.runtime.client_value_collection import (
    ClientValueCollection as ClientValueCollection,
)

class EmailProperties(ClientValue):
    Body: Incomplete
    Subject: Incomplete
    From: Incomplete
    To: Incomplete
    CC: Incomplete
    BCC: Incomplete
    AdditionalHeaders: Incomplete
    def __init__(
        self,
        body,
        subject,
        to,
        from_address: Incomplete | None = None,
        cc: Incomplete | None = None,
        bcc: Incomplete | None = None,
        additional_headers: Incomplete | None = None,
    ) -> None: ...
    @property
    def entity_type_name(self): ...
