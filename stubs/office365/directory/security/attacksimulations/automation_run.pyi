from office365.entity import Entity as Entity

class SimulationAutomationRun(Entity):
    @property
    def simulation_id(self) -> str | None: ...
