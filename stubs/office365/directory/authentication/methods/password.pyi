from _typeshed import Incomplete
from datetime import datetime
from office365.directory.authentication.methods.method import (
    AuthenticationMethod as AuthenticationMethod,
)

class PasswordAuthenticationMethod(AuthenticationMethod):
    @property
    def created_datetime(self) -> datetime: ...
    @property
    def password(self) -> str | None: ...
    def get_property(self, name, default_value: Incomplete | None = None): ...
