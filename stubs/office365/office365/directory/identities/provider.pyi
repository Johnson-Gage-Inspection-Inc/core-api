from office365.entity import Entity as Entity

class IdentityProvider(Entity):
    @property
    def client_id(self) -> str | None: ...
    @property
    def client_secret(self) -> str | None: ...
