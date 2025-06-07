from office365.directory.authentication.methods.method import (
    AuthenticationMethod as AuthenticationMethod,
)

class Fido2AuthenticationMethod(AuthenticationMethod):
    @property
    def model(self) -> str | None: ...
