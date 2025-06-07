from office365.sharepoint.entity import Entity as Entity

class FeatureDefinition(Entity):
    @property
    def display_name(self) -> str | None: ...
