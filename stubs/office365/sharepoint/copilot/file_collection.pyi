from _typeshed import Incomplete
from office365.runtime.client_result import ClientResult as ClientResult
from office365.runtime.queries.service_operation import ServiceOperationQuery as ServiceOperationQuery
from office365.sharepoint.copilot.file_collection_query_result import CopilotFileCollectionQueryResult as CopilotFileCollectionQueryResult
from office365.sharepoint.entity import Entity as Entity

class CopilotFileCollection(Entity):
    @staticmethod
    def get_working_set_files(context, top: Incomplete | None = None, order_by: Incomplete | None = None, skip_token: Incomplete | None = None): ...
