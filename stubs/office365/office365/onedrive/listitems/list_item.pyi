from _typeshed import Incomplete
from office365.entity_collection import EntityCollection as EntityCollection
from office365.onedrive.analytics.item_analytics import ItemAnalytics as ItemAnalytics
from office365.onedrive.base_item import BaseItem as BaseItem
from office365.onedrive.contenttypes.info import ContentTypeInfo as ContentTypeInfo
from office365.onedrive.documentsets.version import (
    DocumentSetVersion as DocumentSetVersion,
)
from office365.onedrive.internal.queries.get_activities_by_interval import (
    build_get_activities_by_interval_query as build_get_activities_by_interval_query,
)
from office365.onedrive.listitems.field_value_set import FieldValueSet as FieldValueSet
from office365.onedrive.versions.list_item import ListItemVersion as ListItemVersion
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath

class ListItem(BaseItem):
    def get_activities_by_interval(
        self,
        start_dt: Incomplete | None = None,
        end_dt: Incomplete | None = None,
        interval: Incomplete | None = None,
    ): ...
    @property
    def fields(self): ...
    @property
    def versions(self) -> EntityCollection[ListItemVersion]: ...
    @property
    def drive_item(self): ...
    @property
    def content_type(self) -> ContentTypeInfo: ...
    @property
    def analytics(self): ...
    @property
    def document_set_versions(self) -> EntityCollection[DocumentSetVersion]: ...
    def get_property(self, name, default_value: Incomplete | None = None): ...
