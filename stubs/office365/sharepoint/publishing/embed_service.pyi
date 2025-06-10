from office365.runtime.queries.service_operation import (
    ServiceOperationQuery as ServiceOperationQuery,
)
from office365.sharepoint.entity import Entity as Entity
from office365.sharepoint.publishing.embed_data_v1 import EmbedDataV1 as EmbedDataV1

class EmbedService(Entity):
    def embed_data(self, url, version: int = 1): ...
    @property
    def entity_type_name(self): ...
