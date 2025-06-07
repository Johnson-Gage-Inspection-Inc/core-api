from office365.directory.security.attacksimulations.repeat_offender import AttackSimulationRepeatOffender as AttackSimulationRepeatOffender
from office365.directory.security.attacksimulations.user_coverage import AttackSimulationSimulationUserCoverage as AttackSimulationSimulationUserCoverage
from office365.entity import Entity as Entity
from office365.runtime.client_result import ClientResult as ClientResult
from office365.runtime.client_value_collection import ClientValueCollection as ClientValueCollection
from office365.runtime.queries.function import FunctionQuery as FunctionQuery

class SecurityReportsRoot(Entity):
    def get_attack_simulation_repeat_offenders(self): ...
    def get_attack_simulation_simulation_user_coverage(self): ...
