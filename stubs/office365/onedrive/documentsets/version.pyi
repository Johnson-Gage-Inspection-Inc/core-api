import datetime

from _typeshed import Incomplete
from office365.directory.permissions.identity_set import IdentitySet as IdentitySet
from office365.onedrive.documentsets.version_item import (
    DocumentSetVersionItem as DocumentSetVersionItem,
)
from office365.onedrive.versions.list_item import ListItemVersion as ListItemVersion
from office365.runtime.client_value_collection import (
    ClientValueCollection as ClientValueCollection,
)

class DocumentSetVersion(ListItemVersion):
    @property
    def comment(self) -> str | None: ...
    @property
    def created_by(self) -> IdentitySet: ...
    @property
    def created_datetime(self) -> datetime.datetime: ...
    @property
    def items(self) -> ClientValueCollection[DocumentSetVersionItem]: ...
    @property
    def should_capture_minor_version(self) -> bool | None: ...
    def get_property(self, name, default_value: Incomplete | None = None): ...
