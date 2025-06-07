from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class ListItemCreationInformation(ClientValue):
    FolderUrl: Incomplete
    LeafName: Incomplete
    UnderlyingObjectType: Incomplete
    def __init__(self, leaf_name: Incomplete | None = None, folder_url: Incomplete | None = None, underlying_object_type: Incomplete | None = None) -> None: ...
