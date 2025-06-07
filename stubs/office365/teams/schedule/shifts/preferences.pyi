from office365.runtime.client_value_collection import ClientValueCollection as ClientValueCollection
from office365.teams.schedule.change_tracked_entity import ChangeTrackedEntity as ChangeTrackedEntity
from office365.teams.schedule.shifts.availability import ShiftAvailability as ShiftAvailability

class ShiftPreferences(ChangeTrackedEntity):
    @property
    def availability(self): ...
