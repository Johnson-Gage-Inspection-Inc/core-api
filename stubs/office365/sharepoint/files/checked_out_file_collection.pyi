from _typeshed import Incomplete
from office365.runtime.queries.service_operation import ServiceOperationQuery as ServiceOperationQuery
from office365.sharepoint.entity_collection import EntityCollection as EntityCollection
from office365.sharepoint.files.checked_out_file import CheckedOutFile as CheckedOutFile

class CheckedOutFileCollection(EntityCollection[CheckedOutFile]):
    def __init__(self, context, resource_path: Incomplete | None = None) -> None: ...
    def get_by_path(self, decoded_url): ...
