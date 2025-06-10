from _typeshed import Incomplete
from datetime import datetime
from office365.entity_collection import EntityCollection as EntityCollection
from office365.onedrive.analytics.item_activity_stat import (
    ItemActivityStat as ItemActivityStat,
)
from office365.onedrive.analytics.item_analytics import ItemAnalytics as ItemAnalytics
from office365.onedrive.base_item import BaseItem as BaseItem
from office365.onedrive.columns.definition_collection import (
    ColumnDefinitionCollection as ColumnDefinitionCollection,
)
from office365.onedrive.contenttypes.collection import (
    ContentTypeCollection as ContentTypeCollection,
)
from office365.onedrive.drives.drive import Drive as Drive
from office365.onedrive.listitems.list_item import ListItem as ListItem
from office365.onedrive.lists.collection import ListCollection as ListCollection
from office365.onedrive.operations.rich_long_running import (
    RichLongRunningOperation as RichLongRunningOperation,
)
from office365.onedrive.permissions.collection import (
    PermissionCollection as PermissionCollection,
)
from office365.onedrive.sharepoint_ids import SharePointIds as SharePointIds
from office365.onedrive.sitepages.collection import (
    SitePageCollection as SitePageCollection,
)
from office365.onedrive.sites.site_collection import SiteCollection as SiteCollection
from office365.onedrive.termstore.store import Store as Store
from office365.onenote.onenote import Onenote as Onenote
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath
from office365.runtime.queries.function import FunctionQuery as FunctionQuery
from office365.runtime.queries.service_operation import (
    ServiceOperationQuery as ServiceOperationQuery,
)

class Site(BaseItem):
    def get_by_path(self, path: str) -> Site: ...
    def get_applicable_content_types_for_list(
        self, list_id: str
    ) -> ContentTypeCollection: ...
    def get_activities_by_interval(
        self,
        start_dt: datetime | None = None,
        end_dt: datetime | None = None,
        interval: str = None,
    ) -> EntityCollection[ItemActivityStat]: ...
    @property
    def site_collection(self) -> SiteCollection: ...
    @property
    def sharepoint_ids(self) -> SharePointIds: ...
    @property
    def items(self) -> EntityCollection[ListItem]: ...
    @property
    def columns(self) -> ColumnDefinitionCollection: ...
    @property
    def external_columns(self) -> ColumnDefinitionCollection: ...
    @property
    def content_types(self) -> ContentTypeCollection: ...
    @property
    def lists(self) -> ListCollection: ...
    @property
    def operations(self) -> EntityCollection[RichLongRunningOperation]: ...
    @property
    def permissions(self) -> PermissionCollection: ...
    @property
    def drive(self) -> Drive: ...
    @property
    def drives(self) -> EntityCollection[Drive]: ...
    @property
    def sites(self) -> EntityCollection[Site]: ...
    @property
    def analytics(self) -> ItemAnalytics: ...
    @property
    def onenote(self) -> Onenote: ...
    @property
    def pages(self) -> SitePageCollection: ...
    @property
    def term_store(self) -> Store: ...
    @property
    def term_stores(self) -> EntityCollection[Store]: ...
    def get_property(self, name, default_value: Incomplete | None = None): ...
