from _typeshed import Incomplete
from office365.directory.synchronization.progress import (
    SynchronizationProgress as SynchronizationProgress,
)
from office365.directory.synchronization.quarantine import (
    SynchronizationQuarantine as SynchronizationQuarantine,
)
from office365.directory.synchronization.task_execution import (
    SynchronizationTaskExecution as SynchronizationTaskExecution,
)
from office365.runtime.client_value import ClientValue as ClientValue
from office365.runtime.client_value_collection import (
    ClientValueCollection as ClientValueCollection,
)

class SynchronizationStatus(ClientValue):
    progress: Incomplete
    quarantine: Incomplete
    lastExecution: Incomplete
    lastSuccessfulExecution: Incomplete
    lastSuccessfulExecutionWithExports: Incomplete
    def __init__(
        self,
        progress: Incomplete | None = None,
        quarantine=...,
        last_execution=...,
        last_successful_execution=...,
        last_successful_execution_with_exports=...,
    ) -> None: ...
