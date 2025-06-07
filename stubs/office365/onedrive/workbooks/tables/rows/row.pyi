from office365.entity import Entity as Entity

class WorkbookTableRow(Entity):
    @property
    def index(self) -> int | None: ...
    @property
    def values(self) -> list | None: ...
