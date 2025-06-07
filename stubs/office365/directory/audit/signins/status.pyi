from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class SignInStatus(ClientValue):
    additionalDetails: Incomplete
    errorCode: Incomplete
    failureReason: Incomplete
    def __init__(self, additional_details: Incomplete | None = None, error_code: Incomplete | None = None, failure_reason: Incomplete | None = None) -> None: ...
