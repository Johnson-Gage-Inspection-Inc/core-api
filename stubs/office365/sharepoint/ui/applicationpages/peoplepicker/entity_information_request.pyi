from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class PickerEntityInformationRequest(ClientValue):
    EmailAddress: Incomplete
    GroupId: Incomplete
    Key: Incomplete
    PrincipalType: Incomplete
    def __init__(self, email_address: Incomplete | None = None, group_id: Incomplete | None = None, key: Incomplete | None = None, principal_type: int = 0) -> None: ...
    @property
    def entity_type_name(self): ...
