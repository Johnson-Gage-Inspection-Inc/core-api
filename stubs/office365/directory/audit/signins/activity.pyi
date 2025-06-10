from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class SignInActivity(ClientValue):
    lastNonInteractiveSignInDateTime: Incomplete
    lastNonInteractiveSignInRequestId: Incomplete
    lastSignInDateTime: Incomplete
    lastSignInRequestId: Incomplete
    def __init__(
        self,
        last_non_interactive_sign_in_datetime: Incomplete | None = None,
        last_non_interactive_sign_in_request_id: Incomplete | None = None,
        last_sign_in_datetime: Incomplete | None = None,
        last_sign_in_request_id: Incomplete | None = None,
    ) -> None: ...
