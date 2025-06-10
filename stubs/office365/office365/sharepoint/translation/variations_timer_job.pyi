from office365.runtime.client_value_collection import (
    ClientValueCollection as ClientValueCollection,
)
from office365.runtime.queries.service_operation import (
    ServiceOperationQuery as ServiceOperationQuery,
)
from office365.sharepoint.entity import Entity as Entity

class VariationsTranslationTimerJob(Entity):
    @staticmethod
    def export_items(context, list_url, item_ids, addresses_to_email): ...
    @property
    def entity_type_name(self): ...
