from office365.entity import Entity as Entity

class WorkbookRangeFill(Entity):
    @property
    def color(self) -> str | None: ...
