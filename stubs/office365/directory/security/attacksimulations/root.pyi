from _typeshed import Incomplete
from office365.directory.security.attacksimulations.automation import SimulationAutomation as SimulationAutomation
from office365.directory.security.attacksimulations.landing_page import LandingPage as LandingPage
from office365.directory.security.attacksimulations.operation import AttackSimulationOperation as AttackSimulationOperation
from office365.directory.security.attacksimulations.simulation import Simulation as Simulation
from office365.entity import Entity as Entity
from office365.entity_collection import EntityCollection as EntityCollection
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath

class AttackSimulationRoot(Entity):
    @property
    def landing_pages(self) -> EntityCollection[LandingPage]: ...
    @property
    def operations(self) -> EntityCollection[AttackSimulationOperation]: ...
    @property
    def simulations(self) -> EntityCollection[Simulation]: ...
    @property
    def simulation_automations(self) -> EntityCollection[SimulationAutomation]: ...
    def get_property(self, name, default_value: Incomplete | None = None): ...
