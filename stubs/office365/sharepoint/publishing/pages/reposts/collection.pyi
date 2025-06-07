from _typeshed import Incomplete
from office365.runtime.client_result import ClientResult as ClientResult
from office365.runtime.queries.service_operation import ServiceOperationQuery as ServiceOperationQuery
from office365.sharepoint.entity_collection import EntityCollection as EntityCollection
from office365.sharepoint.publishing.pages.reposts.repost import RepostPage as RepostPage

class RepostPageCollection(EntityCollection):
    def __init__(self, context, resource_path: Incomplete | None = None) -> None: ...
    def is_content_type_available(self): ...
