from office365.directory.authentication.methods.method import (
    AuthenticationMethod as AuthenticationMethod,
)
from office365.runtime.queries.service_operation import (
    ServiceOperationQuery as ServiceOperationQuery,
)

class PhoneAuthenticationMethod(AuthenticationMethod):
    def disable_sms_signin(self): ...
    def enable_sms_signin(self): ...
    @property
    def phone_number(self): ...
