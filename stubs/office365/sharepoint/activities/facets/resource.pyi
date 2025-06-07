from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class ResourceFacet(ClientValue):
    contentTypeId: Incomplete
    fileSystemObjectType: Incomplete
    fileType: Incomplete
    itemId: Incomplete
    itemUniqueId: Incomplete
    listId: Incomplete
    orgId: Incomplete
    serverRelativePath: Incomplete
    siteId: Incomplete
    title: Incomplete
    webId: Incomplete
    def __init__(self, content_type_id: Incomplete | None = None, file_system_object_type: Incomplete | None = None, file_type: Incomplete | None = None, item_id: Incomplete | None = None, item_unique_id: Incomplete | None = None, list_id: Incomplete | None = None, org_id: Incomplete | None = None, server_relative_path=..., site_id: Incomplete | None = None, title: Incomplete | None = None, web_id: Incomplete | None = None) -> None: ...
    @property
    def entity_type_name(self): ...
