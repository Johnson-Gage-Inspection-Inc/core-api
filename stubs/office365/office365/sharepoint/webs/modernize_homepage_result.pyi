from office365.sharepoint.entity import Entity as Entity

class ModernizeHomepageResult(Entity):
    @property
    def can_modernize_homepage(self) -> bool | None: ...
