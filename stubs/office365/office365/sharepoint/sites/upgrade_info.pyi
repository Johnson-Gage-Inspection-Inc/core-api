from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class UpgradeInfo(ClientValue):
    ErrorFile: Incomplete
    Errors: Incomplete
    LastUpdated: Incomplete
    LogFile: Incomplete
    RequestDate: Incomplete
    RetryCount: Incomplete
    StartTime: Incomplete
    Status: Incomplete
    UpgradeType: Incomplete
    Warnings: Incomplete
    def __init__(
        self,
        error_file: Incomplete | None = None,
        errors: Incomplete | None = None,
        last_updated=...,
        log_file: Incomplete | None = None,
        request_date=...,
        retry_count: Incomplete | None = None,
        start_time=...,
        status: Incomplete | None = None,
        upgrade_type: Incomplete | None = None,
        warnings: Incomplete | None = None,
    ) -> None: ...
