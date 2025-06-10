from _typeshed import Incomplete
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath
from office365.runtime.queries.service_operation import (
    ServiceOperationQuery as ServiceOperationQuery,
)
from office365.sharepoint.entity import Entity as Entity

class DocumentId(Entity):
    def __init__(self, context) -> None: ...
    def reset_docid_by_server_relative_path(self, decoded_url): ...
    def reset_doc_ids_in_library(
        self, decoded_url, content_type_id: Incomplete | None = None
    ): ...
    def set_doc_id_site_prefix(
        self, prefix, schedule_assignment, overwrite_existing_ids
    ): ...
    @property
    def entity_type_name(self): ...
    @property
    def entity_type_id(self): ...
