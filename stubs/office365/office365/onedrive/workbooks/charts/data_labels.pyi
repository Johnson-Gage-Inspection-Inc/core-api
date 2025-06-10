from office365.entity import Entity as Entity

class WorkbookChartDataLabels(Entity):
    @property
    def position(self) -> str | None: ...
    @property
    def separator(self) -> str | None: ...
