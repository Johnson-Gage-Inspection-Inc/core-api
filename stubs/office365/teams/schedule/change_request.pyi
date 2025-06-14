from office365.runtime.queries.service_operation import (
    ServiceOperationQuery as ServiceOperationQuery,
)
from office365.teams.schedule.change_tracked_entity import (
    ChangeTrackedEntity as ChangeTrackedEntity,
)

class ScheduleChangeRequest(ChangeTrackedEntity):
    def approve(self, message): ...
    def decline(self, message): ...
