from office365.runtime.client_result import ClientResult as ClientResult
from office365.runtime.queries.service_operation import ServiceOperationQuery as ServiceOperationQuery
from office365.sharepoint.entity import Entity as Entity
from typing import AnyStr

class TeamsPackageDownload(Entity):
    def download_teams(self) -> ClientResult[AnyStr]: ...
    @property
    def entity_type_name(self): ...
