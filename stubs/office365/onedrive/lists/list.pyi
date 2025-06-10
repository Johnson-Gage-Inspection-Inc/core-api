from _typeshed import Incomplete
from office365.entity_collection import EntityCollection as EntityCollection
from office365.onedrive.base_item import BaseItem as BaseItem
from office365.onedrive.columns.definition_collection import (
    ColumnDefinitionCollection as ColumnDefinitionCollection,
)
from office365.onedrive.contenttypes.collection import (
    ContentTypeCollection as ContentTypeCollection,
)
from office365.onedrive.listitems.collection import (
    ListItemCollection as ListItemCollection,
)
from office365.onedrive.lists.info import ListInfo as ListInfo
from office365.onedrive.operations.rich_long_running import (
    RichLongRunningOperation as RichLongRunningOperation,
)
from office365.onedrive.sharepoint_ids import SharePointIds as SharePointIds
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath
from office365.subscriptions.subscription import Subscription as Subscription

class List(BaseItem):
    @property
    def display_name(self) -> str | None: ...
    @property
    def list(self): ...
    @property
    def sharepoint_ids(self): ...
    @property
    def drive(self): ...
    @property
    def columns(self) -> ColumnDefinitionCollection: ...
    @property
    def content_types(self) -> ContentTypeCollection: ...
    @property
    def items(self) -> ListItemCollection: ...
    @property
    def operations(self) -> EntityCollection[RichLongRunningOperation]: ...
    @property
    def subscriptions(self) -> EntityCollection[Subscription]: ...
    def get_property(self, name, default_value: Incomplete | None = None): ...
