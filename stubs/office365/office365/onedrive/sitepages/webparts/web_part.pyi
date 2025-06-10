from office365.entity import Entity as Entity
from office365.onedrive.sitepages.webparts.position import (
    WebPartPosition as WebPartPosition,
)
from office365.runtime.client_result import ClientResult as ClientResult
from office365.runtime.queries.service_operation import (
    ServiceOperationQuery as ServiceOperationQuery,
)

class WebPart(Entity):
    def get_position_of_web_part(self): ...
