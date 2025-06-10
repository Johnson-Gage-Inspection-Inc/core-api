from _typeshed import Incomplete
from office365.directory.permissions.identity import Identity as Identity
from office365.runtime.client_value import ClientValue as ClientValue

class IdentitySet(ClientValue):
    application: Incomplete
    device: Incomplete
    user: Incomplete
    def __init__(self, application=..., device=..., user=...) -> None: ...
