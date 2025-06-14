from _typeshed import Incomplete
from office365.runtime.client_value_collection import (
    ClientValueCollection as ClientValueCollection,
)
from office365.sharepoint.entity import Entity as Entity
from office365.sharepoint.sharing.shared_with_user import (
    SharedWithUser as SharedWithUser,
)

class FileVersionEvent(Entity):
    @property
    def event_type(self) -> str | None: ...
    @property
    def editor(self) -> str | None: ...
    @property
    def shared_by_user(self): ...
    @property
    def shared_with_users(self) -> ClientValueCollection[SharedWithUser]: ...
    def get_property(self, name, default_value: Incomplete | None = None): ...
