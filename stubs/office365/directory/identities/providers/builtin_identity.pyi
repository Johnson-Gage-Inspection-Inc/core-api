from office365.directory.identities.providers.base import IdentityProviderBase as IdentityProviderBase

class BuiltInIdentityProvider(IdentityProviderBase):
    @property
    def identity_provider_type(self) -> str | None: ...
