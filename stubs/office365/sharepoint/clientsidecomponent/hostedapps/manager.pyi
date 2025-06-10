from office365.runtime.paths.service_operation import (
    ServiceOperationPath as ServiceOperationPath,
)
from office365.sharepoint.clientsidecomponent.hostedapps.app import (
    HostedApp as HostedApp,
)
from office365.sharepoint.entity import Entity as Entity

class HostedAppsManager(Entity):
    def get_by_id(self, id_): ...
    @property
    def entity_type_name(self): ...
