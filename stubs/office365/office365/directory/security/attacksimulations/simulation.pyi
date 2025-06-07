from office365.directory.security.attacksimulations.report import (
    SimulationReport as SimulationReport,
)
from office365.entity import Entity as Entity

class Simulation(Entity):
    @property
    def report(self): ...
