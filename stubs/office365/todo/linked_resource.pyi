from office365.entity import Entity as Entity

class LinkedResource(Entity):
    @property
    def application_name(self) -> str | None: ...
    @property
    def display_name(self) -> str | None: ...
