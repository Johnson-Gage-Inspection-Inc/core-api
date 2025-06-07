from _typeshed import Incomplete
from office365.directory.policies.conditional_access import ConditionalAccessPolicy as ConditionalAccessPolicy
from office365.runtime.client_value import ClientValue as ClientValue
from office365.runtime.client_value_collection import ClientValueCollection as ClientValueCollection

class AuthenticationStrengthUsage(ClientValue):
    mfa: Incomplete
    none: Incomplete
    def __init__(self, mfa: Incomplete | None = None, none: Incomplete | None = None) -> None: ...
