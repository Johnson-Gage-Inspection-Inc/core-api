from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class TeamSummary(ClientValue):
    guestsCount: Incomplete
    membersCount: Incomplete
    ownersCount: Incomplete
    def __init__(
        self,
        guests_count: Incomplete | None = None,
        members_count: Incomplete | None = None,
        owners_count: Incomplete | None = None,
    ) -> None: ...
