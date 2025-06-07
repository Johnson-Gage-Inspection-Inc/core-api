from office365.entity import Entity as Entity

class OutlookCategory(Entity):
    @property
    def color(self) -> str | None: ...
    @property
    def display_name(self) -> str | None: ...
