from .throttled_http_client import (
    RetryAfterParser as RetryAfterParser,
    ThrottledHttpClientBase as ThrottledHttpClientBase,
)
from .token_cache import TokenCache as TokenCache
from _typeshed import Incomplete
from collections import UserDict

logger: Incomplete

class ManagedIdentityError(ValueError): ...

class ManagedIdentity(UserDict):
    ID_TYPE: str
    ID: str
    CLIENT_ID: str
    RESOURCE_ID: str
    OBJECT_ID: str
    SYSTEM_ASSIGNED: str
    @classmethod
    def is_managed_identity(cls, unknown): ...
    @classmethod
    def is_system_assigned(cls, unknown): ...
    @classmethod
    def is_user_assigned(cls, unknown): ...
    def __init__(
        self, identifier: Incomplete | None = None, id_type: Incomplete | None = None
    ) -> None: ...

class SystemAssignedManagedIdentity(ManagedIdentity):
    def __init__(self) -> None: ...

class UserAssignedManagedIdentity(ManagedIdentity):
    def __init__(
        self,
        *,
        client_id: Incomplete | None = None,
        resource_id: Incomplete | None = None,
        object_id: Incomplete | None = None,
    ) -> None: ...

class _ThrottledHttpClient(ThrottledHttpClientBase):
    get: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...

class ManagedIdentityClient:
    def __init__(
        self,
        managed_identity: (
            dict
            | ManagedIdentity
            | SystemAssignedManagedIdentity
            | UserAssignedManagedIdentity
        ),
        *,
        http_client,
        token_cache: Incomplete | None = None,
        http_cache: Incomplete | None = None,
    ) -> None: ...
    def acquire_token_for_client(
        self, *, resource: str, claims_challenge: str | None = None
    ): ...

APP_SERVICE: Incomplete
AZURE_ARC: Incomplete
CLOUD_SHELL: Incomplete
MACHINE_LEARNING: Incomplete
SERVICE_FABRIC: Incomplete
DEFAULT_TO_VM: Incomplete

def get_managed_identity_source(): ...

class ArcPlatformNotSupportedError(ManagedIdentityError): ...
