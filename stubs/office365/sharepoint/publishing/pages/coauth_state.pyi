from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class SitePageCoAuthState(ClientValue):
    Action: Incomplete
    HasReachedMinorVersionsLimit: Incomplete
    IsNewSession: Incomplete
    IsPartitionFlushed: Incomplete
    LockAction: Incomplete
    LockDuration: Incomplete
    OverwriteExistingVersion: Incomplete
    SharedLockId: Incomplete
    def __init__(
        self,
        action: Incomplete | None = None,
        has_reached_minor_versions_limit: Incomplete | None = None,
        is_new_session: Incomplete | None = None,
        is_partition_flushed: Incomplete | None = None,
        lock_action: Incomplete | None = None,
        lock_duration: Incomplete | None = None,
        overwrite_existing_version: Incomplete | None = None,
        shared_lock_id: Incomplete | None = None,
    ) -> None: ...
    @property
    def entity_type_name(self): ...
