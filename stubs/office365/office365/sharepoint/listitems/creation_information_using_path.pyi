from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class ListItemCreationInformationUsingPath(ClientValue):
    LeafName: Incomplete
    UnderlyingObjectType: Incomplete
    FolderPath: Incomplete
    def __init__(
        self, leaf_name, object_type, folder_path: Incomplete | None = None
    ) -> None: ...
