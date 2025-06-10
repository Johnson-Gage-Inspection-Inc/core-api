from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class AttackSimulationUser(ClientValue):
    displayName: Incomplete
    email: Incomplete
    userId: Incomplete
    def __init__(
        self,
        display_name: Incomplete | None = None,
        email: Incomplete | None = None,
        user_id: Incomplete | None = None,
    ) -> None: ...
