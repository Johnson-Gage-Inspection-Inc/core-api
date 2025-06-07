from _typeshed import Incomplete
from office365.runtime.client_result import ClientResult as ClientResult
from office365.runtime.queries.service_operation import ServiceOperationQuery as ServiceOperationQuery
from office365.sharepoint.entity import Entity as Entity
from office365.sharepoint.navigation.configured_metadata_items import ConfiguredMetadataNavigationItemCollection as ConfiguredMetadataNavigationItemCollection

class MetadataNavigationSettings(Entity):
    @staticmethod
    def get_configured_settings(context, url, return_type: Incomplete | None = None): ...
    @property
    def entity_type_name(self): ...
