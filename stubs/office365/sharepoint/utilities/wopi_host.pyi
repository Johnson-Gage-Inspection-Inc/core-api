from office365.runtime.client_result import ClientResult as ClientResult
from office365.runtime.client_value_collection import ClientValueCollection as ClientValueCollection
from office365.runtime.queries.service_operation import ServiceOperationQuery as ServiceOperationQuery
from office365.sharepoint.client_context import ClientContext as ClientContext
from office365.sharepoint.entity import Entity as Entity

class WopiHostUtility(Entity):
    @staticmethod
    def generate_file_bundle(context: ClientContext) -> ClientResult[str]: ...
    @staticmethod
    def get_wopi_origins(context): ...
    @property
    def entity_type_name(self): ...
