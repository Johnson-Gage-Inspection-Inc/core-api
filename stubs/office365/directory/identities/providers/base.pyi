from office365.entity import Entity as Entity

class IdentityProviderBase(Entity):
    @property
    def display_name(self) -> str | None: ...
