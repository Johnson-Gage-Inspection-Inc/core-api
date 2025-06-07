from office365.sharepoint.entity import Entity as Entity

class SiteDesignRun(Entity):
    @property
    def site_design_id(self) -> str | None: ...
    @property
    def entity_type_name(self): ...
