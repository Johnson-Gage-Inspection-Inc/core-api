from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class SharedWithMeDocumentUser(ClientValue):
    Id: Incomplete
    LoginName: Incomplete
    SipAddress: Incomplete
    Title: Incomplete
    def __init__(self, _id: Incomplete | None = None, login_name: Incomplete | None = None, sip_address: Incomplete | None = None, title: Incomplete | None = None) -> None: ...
    @property
    def entity_type_name(self): ...
