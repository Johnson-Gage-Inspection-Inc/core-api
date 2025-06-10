from _typeshed import Incomplete
from office365.directory.security.attacksimulations.user import (
    AttackSimulationUser as AttackSimulationUser,
)
from office365.runtime.client_value import ClientValue as ClientValue

class AttackSimulationRepeatOffender(ClientValue):
    attackSimulationUser: Incomplete
    repeatOffenceCount: Incomplete
    def __init__(
        self, attack_simulation_user=..., repeat_offence_count: Incomplete | None = None
    ) -> None: ...
