from _typeshed import Incomplete
from office365.entity import Entity as Entity

class TeamsAsyncOperation(Entity):
    def poll_for_status(
        self,
        status_type: str = "succeeded",
        max_polling_count: int = 5,
        polling_interval_secs: int = 15,
        success_callback: Incomplete | None = None,
        failure_callback: Incomplete | None = None,
    ): ...
    @property
    def target_resource_id(self) -> str | None: ...
    @property
    def target_resource_location(self) -> str | None: ...
    @property
    def status(self) -> str | None: ...
