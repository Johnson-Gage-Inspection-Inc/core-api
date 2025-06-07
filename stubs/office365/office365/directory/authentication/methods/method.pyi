from office365.directory.authentication.password_reset_response import (
    PasswordResetResponse as PasswordResetResponse,
)
from office365.entity import Entity as Entity
from office365.runtime.client_result import ClientResult as ClientResult
from office365.runtime.queries.service_operation import (
    ServiceOperationQuery as ServiceOperationQuery,
)

class AuthenticationMethod(Entity):
    def reset_password(self, new_password, require_change_on_next_signin): ...
