from office365.onedrive.operations.long_running import (
    LongRunningOperation as LongRunningOperation,
)

class RichLongRunningOperation(LongRunningOperation):
    @property
    def resource_id(self) -> str | None: ...
