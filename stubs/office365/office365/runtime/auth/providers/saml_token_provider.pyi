import office365.logger
from _typeshed import Incomplete
from office365.runtime.auth.auth_cookies import AuthCookies as AuthCookies
from office365.runtime.auth.authentication_provider import (
    AuthenticationProvider as AuthenticationProvider,
)
from office365.runtime.auth.sts_profile import STSProfile as STSProfile
from office365.runtime.auth.user_realm_info import UserRealmInfo as UserRealmInfo

def string_escape(value): ...
def datetime_escape(value): ...

class SamlTokenProvider(AuthenticationProvider, office365.logger.LoggerContext):
    error: str
    def __init__(
        self,
        url,
        username,
        password,
        browser_mode,
        environment: Incomplete | None = None,
    ) -> None: ...
    def authenticate_request(self, request) -> None: ...
    def get_authentication_cookie(self): ...
