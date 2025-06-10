from office365.runtime.client_result import ClientResult as ClientResult
from office365.runtime.http.http_method import HttpMethod as HttpMethod
from office365.runtime.http.request_options import RequestOptions as RequestOptions
from office365.runtime.queries.service_operation import (
    ServiceOperationQuery as ServiceOperationQuery,
)
from office365.sharepoint.entity import Entity as Entity
from typing import AnyStr

class GroupService(Entity):
    def get_group_image(
        self,
        group_id: str,
        image_hash: str = None,
        image_color: str = None,
        return_type: ClientResult = None,
    ) -> ClientResult[AnyStr]: ...
    def sync_group_properties(self): ...
    @property
    def entity_type_name(self): ...
