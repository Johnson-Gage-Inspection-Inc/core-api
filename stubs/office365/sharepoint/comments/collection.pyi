from _typeshed import Incomplete
from office365.runtime.client_result import ClientResult as ClientResult
from office365.runtime.queries.service_operation import ServiceOperationQuery as ServiceOperationQuery
from office365.sharepoint.comments.comment import Comment as Comment
from office365.sharepoint.entity_collection import EntityCollection as EntityCollection

class CommentCollection(EntityCollection[Comment]):
    def __init__(self, context, resource_path: Incomplete | None = None) -> None: ...
    def delete_all(self): ...
