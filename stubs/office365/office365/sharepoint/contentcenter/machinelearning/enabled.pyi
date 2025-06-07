from office365.sharepoint.entity import Entity as Entity

class SPMachineLearningEnabled(Entity):
    @property
    def is_syntex_payg_enabled(self) -> bool | None: ...
    @property
    def entity_type_name(self): ...
