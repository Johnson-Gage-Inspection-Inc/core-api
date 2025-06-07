from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class RecycleBinSettings(ClientValue):
    retentionPeriodOverrideDays: Incomplete
    def __init__(
        self, retention_period_override_days: Incomplete | None = None
    ) -> None: ...
