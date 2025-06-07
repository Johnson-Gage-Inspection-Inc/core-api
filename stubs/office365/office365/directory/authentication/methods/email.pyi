from office365.directory.authentication.methods.method import (
    AuthenticationMethod as AuthenticationMethod,
)

class EmailAuthenticationMethod(AuthenticationMethod):
    @property
    def email_address(self) -> str | None: ...
