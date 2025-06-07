from _typeshed import Incomplete

logger: Incomplete
AZURE_US_GOVERNMENT: str
AZURE_CHINA: str
AZURE_PUBLIC: str
WORLD_WIDE: str
WELL_KNOWN_AUTHORITY_HOSTS: Incomplete
WELL_KNOWN_B2C_HOSTS: Incomplete

class AuthorityBuilder:
    def __init__(self, instance, tenant) -> None: ...

class Authority:
    authorization_endpoint: Incomplete
    token_endpoint: Incomplete
    device_authorization_endpoint: Incomplete
    def __init__(self, authority_url, http_client, validate_authority: bool = True, instance_discovery: Incomplete | None = None, oidc_authority_url: Incomplete | None = None) -> None: ...
    def user_realm_discovery(self, username, correlation_id: Incomplete | None = None, response: Incomplete | None = None): ...

def canonicalize(authority_or_auth_endpoint): ...
def tenant_discovery(tenant_discovery_endpoint, http_client, **kwargs): ...
