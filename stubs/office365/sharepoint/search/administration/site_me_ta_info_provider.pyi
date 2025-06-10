from office365.runtime.client_result import ClientResult as ClientResult
from office365.runtime.queries.service_operation import (
    ServiceOperationQuery as ServiceOperationQuery,
)
from office365.sharepoint.entity import Entity as Entity

class SiteMeTAInfoProvider(Entity):
    def get_azure_container_sas_token(self): ...
    @property
    def entity_type_name(self): ...
