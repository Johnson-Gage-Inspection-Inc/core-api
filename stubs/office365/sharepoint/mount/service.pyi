from office365.runtime.client_result import ClientResult as ClientResult
from office365.runtime.queries.service_operation import (
    ServiceOperationQuery as ServiceOperationQuery,
)
from office365.sharepoint.entity import Entity as Entity
from office365.sharepoint.mount.requests.get_remote_item_Info import (
    GetRemoteItemInfoRequest as GetRemoteItemInfoRequest,
)

class MountService(Entity):
    @staticmethod
    def get_remote_item_info(context, remote_item_unique_ids): ...
    @property
    def entity_type_name(self): ...
