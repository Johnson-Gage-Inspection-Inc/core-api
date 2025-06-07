from office365.runtime.client_result import ClientResult as ClientResult
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath
from office365.runtime.queries.service_operation import ServiceOperationQuery as ServiceOperationQuery
from office365.runtime.types.collections import StringCollection as StringCollection
from office365.sharepoint.entity import Entity as Entity

class ProfileImageStore(Entity):
    def __init__(self, context) -> None: ...
    def save_uploaded_file(self, profile_type, file_name_prefix, is_feed_attachment, client_file_path, file_size, file_stream): ...
    @property
    def entity_type_name(self): ...
