from office365.entity import Entity as Entity

class LongRunningOperation(Entity):
    @property
    def resource_location(self) -> str | None: ...
    @property
    def status_detail(self) -> str | None: ...
