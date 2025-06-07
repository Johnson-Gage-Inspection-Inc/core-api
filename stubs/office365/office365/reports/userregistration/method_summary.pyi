from _typeshed import Incomplete
from office365.reports.userregistration.method_count import (
    UserRegistrationMethodCount as UserRegistrationMethodCount,
)
from office365.runtime.client_value import ClientValue as ClientValue
from office365.runtime.client_value_collection import (
    ClientValueCollection as ClientValueCollection,
)

class UserRegistrationMethodSummary(ClientValue):
    totalUserCount: Incomplete
    userRegistrationMethodCounts: Incomplete
    userRoles: Incomplete
    userTypes: Incomplete
    def __init__(
        self,
        total_user_count: Incomplete | None = None,
        method_counts: Incomplete | None = None,
        user_roles: Incomplete | None = None,
        user_types: Incomplete | None = None,
    ) -> None: ...
