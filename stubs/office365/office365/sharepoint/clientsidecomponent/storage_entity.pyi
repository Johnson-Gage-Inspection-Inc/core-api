from office365.sharepoint.entity import Entity as Entity

class StorageEntity(Entity):
    @property
    def value(self): ...
