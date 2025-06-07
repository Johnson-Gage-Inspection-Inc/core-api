from office365.sharepoint.entity import Entity as Entity

class BaseCustomProperty(Entity):
    @property
    def entity_type_name(self): ...
