from office365.sharepoint.entity import Entity as Entity

class HostedApp(Entity):
    @property
    def entity_type_name(self): ...
