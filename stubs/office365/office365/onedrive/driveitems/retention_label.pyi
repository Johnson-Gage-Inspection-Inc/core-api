from datetime import datetime

from _typeshed import Incomplete
from office365.directory.permissions.identity_set import IdentitySet as IdentitySet
from office365.entity import Entity as Entity
from office365.onedrive.driveitems.retention_label_settings import (
    RetentionLabelSettings as RetentionLabelSettings,
)

class ItemRetentionLabel(Entity):
    @property
    def is_label_applied_explicitly(self) -> bool | None: ...
    @property
    def label_applied_by(self) -> IdentitySet | None: ...
    @property
    def label_applied_datetime(self) -> datetime | None: ...
    @property
    def name(self) -> str | None: ...
    @property
    def retention_settings(self) -> RetentionLabelSettings: ...
    def get_property(self, name, default_value: Incomplete | None = None): ...
