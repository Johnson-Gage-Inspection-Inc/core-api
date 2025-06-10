from office365.sharepoint.entity import Entity as Entity

class SPOWebAppServicePrincipalPermissionRequest(Entity):
    @property
    def client_component_item_unique_id(self): ...
    @property
    def entity_type_name(self): ...
