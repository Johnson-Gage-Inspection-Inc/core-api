from office365.runtime.client_result import ClientResult as ClientResult
from office365.runtime.client_value_collection import (
    ClientValueCollection as ClientValueCollection,
)
from office365.runtime.queries.service_operation import (
    ServiceOperationQuery as ServiceOperationQuery,
)
from office365.sharepoint.entity import Entity as Entity
from office365.sharepoint.webparts.tile_data import TileData as TileData

class SocialAnnouncementManager(Entity):
    @staticmethod
    def get_current_announcements(context, url): ...
    @property
    def entity_type_name(self): ...
