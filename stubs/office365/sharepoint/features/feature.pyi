from office365.sharepoint.entity import Entity as Entity

class Feature(Entity):
    @property
    def definition_id(self) -> str | None: ...
    @property
    def display_name(self) -> str | None: ...
