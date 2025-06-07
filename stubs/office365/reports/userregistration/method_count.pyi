from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class UserRegistrationMethodCount(ClientValue):
    authenticationMethod: Incomplete
    userCount: Incomplete
    def __init__(self, authentication_method: Incomplete | None = None, user_count: Incomplete | None = None) -> None: ...
