from office365.directory.identities.providers.base import (
    IdentityProviderBase as IdentityProviderBase,
)

class SamlOrWsFedProvider(IdentityProviderBase):
    @property
    def issuer_uri(self) -> str | None: ...
