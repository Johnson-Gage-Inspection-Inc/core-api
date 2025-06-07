from office365.sharepoint.entity import Entity as Entity

class EffectiveInformationRightsManagementSettings(Entity):
    @property
    def allow_print(self) -> bool | None: ...
    @property
    def template_id(self) -> str | None: ...
