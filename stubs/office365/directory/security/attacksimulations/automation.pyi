from _typeshed import Incomplete
from office365.directory.permissions.email_identity import EmailIdentity as EmailIdentity
from office365.directory.security.attacksimulations.automation_run import SimulationAutomationRun as SimulationAutomationRun
from office365.entity import Entity as Entity
from office365.entity_collection import EntityCollection as EntityCollection
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath

class SimulationAutomation(Entity):
    @property
    def created_by(self): ...
    @property
    def runs(self): ...
    def get_property(self, name, default_value: Incomplete | None = None): ...
