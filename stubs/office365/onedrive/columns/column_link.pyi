from office365.entity import Entity as Entity

class ColumnLink(Entity):
    @property
    def name(self) -> str | None: ...
