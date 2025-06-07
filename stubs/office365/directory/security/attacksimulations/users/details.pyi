from _typeshed import Incomplete
from office365.directory.security.attacksimulations.user import AttackSimulationUser as AttackSimulationUser
from office365.runtime.client_value import ClientValue as ClientValue

class UserSimulationDetails(ClientValue):
    assignedTrainingsCount: Incomplete
    simulationUser: Incomplete
    def __init__(self, assigned_trainings_count: Incomplete | None = None, simulation_user=...) -> None: ...
