from office365.entity import Entity as Entity

class AuthenticationFlowsPolicy(Entity):
    @property
    def display_name(self) -> str | None: ...
