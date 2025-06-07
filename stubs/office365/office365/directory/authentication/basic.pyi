from _typeshed import Incomplete
from office365.directory.authentication.configuration_base import (
    ApiAuthenticationConfigurationBase as ApiAuthenticationConfigurationBase,
)

class BasicAuthentication(ApiAuthenticationConfigurationBase):
    username: Incomplete
    password: Incomplete
    def __init__(
        self, username: Incomplete | None = None, password: Incomplete | None = None
    ) -> None: ...
