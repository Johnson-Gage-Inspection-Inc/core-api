from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class UserRoleAssignment(ClientValue):
    Role: Incomplete
    UserId: Incomplete
    def __init__(self, role: Incomplete | None = None, user_id: Incomplete | None = None) -> None: ...
    @property
    def entity_type_name(self): ...
