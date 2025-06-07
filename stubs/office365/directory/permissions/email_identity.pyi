from _typeshed import Incomplete
from office365.directory.permissions.identity import Identity as Identity

class EmailIdentity(Identity):
    email: Incomplete
    def __init__(self, id_: Incomplete | None = None, email: Incomplete | None = None, display_name: Incomplete | None = None) -> None: ...
