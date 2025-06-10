from office365.runtime.client_result import ClientResult as ClientResult
from office365.runtime.queries.service_operation import (
    ServiceOperationQuery as ServiceOperationQuery,
)
from office365.sharepoint.entity import Entity as Entity

class VideoItem(Entity):
    def get_video_embed_code(
        self,
        width,
        height,
        autoplay: bool = True,
        show_info: bool = True,
        make_responsive: bool = True,
    ): ...
    def set_video_owner(self, owner_id): ...
    @property
    def entity_type_name(self): ...
