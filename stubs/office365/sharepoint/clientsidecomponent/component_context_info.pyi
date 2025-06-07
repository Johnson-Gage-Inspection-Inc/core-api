from office365.sharepoint.entity import Entity as Entity

class ComponentContextInfo(Entity):
    @property
    def serialized_data(self) -> str | None: ...
    @property
    def entity_type_name(self): ...
