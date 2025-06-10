from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue
from office365.sharepoint.administration.orgassets.library_collection import (
    OrgAssetsLibraryCollection as OrgAssetsLibraryCollection,
)

class OrgAssets(ClientValue):
    OrgAssetsLibraries: Incomplete
    def __init__(self) -> None: ...
    @property
    def entity_type_name(self): ...
