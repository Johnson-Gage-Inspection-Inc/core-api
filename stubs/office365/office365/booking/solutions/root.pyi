from _typeshed import Incomplete
from office365.backuprestore.root import BackupRestoreRoot as BackupRestoreRoot
from office365.booking.business.collection import (
    BookingBusinessCollection as BookingBusinessCollection,
)
from office365.booking.currency import BookingCurrency as BookingCurrency
from office365.entity import Entity as Entity
from office365.entity_collection import EntityCollection as EntityCollection
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath

class SolutionsRoot(Entity):
    @property
    def booking_businesses(self) -> BookingBusinessCollection: ...
    @property
    def booking_currencies(self): ...
    @property
    def backup_restore(self) -> BackupRestoreRoot: ...
    def get_property(self, name, default_value: Incomplete | None = None): ...
