from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue
from office365.sharepoint.administration.orgassets.org_assets import (
    OrgAssets as OrgAssets,
)

class FilePickerOptions(ClientValue):
    BingSearchEnabled: Incomplete
    CentralAssetRepository: Incomplete
    OrgAssets: Incomplete
    def __init__(
        self,
        search_enabled: Incomplete | None = None,
        central_asset_repository=...,
        org_assets=...,
    ) -> None: ...
    @property
    def entity_type_name(self): ...
