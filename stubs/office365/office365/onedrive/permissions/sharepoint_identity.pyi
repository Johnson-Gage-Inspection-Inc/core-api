from _typeshed import Incomplete
from office365.directory.permissions.identity import Identity as Identity

class SharePointIdentity(Identity):
    loginName: Incomplete
    def __init__(self, login_name: Incomplete | None = None) -> None: ...
