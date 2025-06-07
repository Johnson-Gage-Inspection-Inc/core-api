from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class PasswordCredential(ClientValue):
    displayName: Incomplete
    secretText: Incomplete
    keyId: Incomplete
    startDateTime: Incomplete
    endDateTime: Incomplete
    def __init__(self, display_name: Incomplete | None = None, secret_text: Incomplete | None = None, key_id: Incomplete | None = None, start_datetime: Incomplete | None = None, end_datetime: Incomplete | None = None) -> None: ...
