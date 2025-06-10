from _typeshed import Incomplete
from office365.runtime.client_result import ClientResult as ClientResult
from office365.runtime.client_value_collection import (
    ClientValueCollection as ClientValueCollection,
)
from office365.runtime.queries.service_operation import (
    ServiceOperationQuery as ServiceOperationQuery,
)
from office365.sharepoint.entity import Entity as Entity
from office365.sharepoint.webparts.tile_data import TileData as TileData

class PromotedSites(Entity):
    @staticmethod
    def add_site_link(
        context,
        url,
        title,
        description: Incomplete | None = None,
        image_url: Incomplete | None = None,
    ): ...
    @staticmethod
    def delete_site_link(context, item_id): ...
    @staticmethod
    def get_promoted_links_as_tiles(context): ...
    @property
    def entity_type_name(self): ...
