from office365.sharepoint.entity import Entity as Entity

class Audit(Entity):
    @property
    def allow_designer(self) -> bool | None: ...
