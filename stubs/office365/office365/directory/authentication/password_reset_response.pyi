from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class PasswordResetResponse(ClientValue):
    newPassword: Incomplete
    def __init__(self, new_password: Incomplete | None = None) -> None: ...
