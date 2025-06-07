from office365.sharepoint.entity import Entity as Entity

class ConnectorResult(Entity):
    @property
    def context_data(self) -> str | None: ...
    @property
    def value(self) -> str | None: ...
