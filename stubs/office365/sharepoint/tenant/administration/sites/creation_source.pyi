from _typeshed import Incomplete
from datetime import datetime
from office365.runtime.client_value import ClientValue as ClientValue
from office365.runtime.client_value_collection import (
    ClientValueCollection as ClientValueCollection,
)
from office365.sharepoint.tenant.administration.sites.creation_data import (
    SiteCreationData as SiteCreationData,
)

class SiteCreationSource(ClientValue):
    IsSyncThresholdLimitReached: Incomplete
    LastRefreshTimeStamp: Incomplete
    SiteCreationData: Incomplete
    SyncThresholdLimit: Incomplete
    TotalSitesCount: Incomplete
    def __init__(
        self,
        is_sync_threshold_limit_reached: bool = None,
        last_refresh_time_stamp: datetime = None,
        site_creation_data: list[SiteCreationData] = None,
        sync_threshold_limit: int = None,
        total_sites_count: int = None,
    ) -> None: ...
    @property
    def entity_type_name(self): ...
