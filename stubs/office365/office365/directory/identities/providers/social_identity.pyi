from office365.directory.identities.providers.base import (
    IdentityProviderBase as IdentityProviderBase,
)

class SocialIdentityProvider(IdentityProviderBase):
    @property
    def client_id(self) -> str | None: ...
    @property
    def client_secret(self) -> str | None: ...
    @property
    def identity_provider_type(self) -> str | None: ...
