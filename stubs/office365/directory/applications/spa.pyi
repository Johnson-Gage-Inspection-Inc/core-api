from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue
from office365.runtime.types.collections import StringCollection as StringCollection

class SpaApplication(ClientValue):
    redirectUris: Incomplete
    def __init__(self, redirect_uris: Incomplete | None = None) -> None: ...
