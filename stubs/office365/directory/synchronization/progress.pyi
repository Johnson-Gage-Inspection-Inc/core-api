from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class SynchronizationProgress(ClientValue):
    completedUnits: Incomplete
    progressObservationDateTime: Incomplete
    totalUnits: Incomplete
    units: Incomplete
    def __init__(self, completed_units: Incomplete | None = None, progress_observation_date_time: Incomplete | None = None, total_units: Incomplete | None = None, units: Incomplete | None = None) -> None: ...
