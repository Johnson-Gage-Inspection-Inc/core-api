from _typeshed import Incomplete
from office365.directory.security.alerts.alert import Alert as Alert
from office365.directory.security.alerts.collection import AlertCollection as AlertCollection
from office365.directory.security.attacksimulations.root import AttackSimulationRoot as AttackSimulationRoot
from office365.directory.security.cases.root import CasesRoot as CasesRoot
from office365.directory.security.hunting_query_results import HuntingQueryResults as HuntingQueryResults
from office365.directory.security.incidents.incident import Incident as Incident
from office365.directory.security.scorecontrol.profile import SecureScoreControlProfile as SecureScoreControlProfile
from office365.directory.security.threatintelligence.threat_intelligence import ThreatIntelligence as ThreatIntelligence
from office365.directory.security.triggers.root import TriggersRoot as TriggersRoot
from office365.entity import Entity as Entity
from office365.entity_collection import EntityCollection as EntityCollection
from office365.runtime.client_result import ClientResult as ClientResult
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath
from office365.runtime.queries.service_operation import ServiceOperationQuery as ServiceOperationQuery

class Security(Entity):
    def run_hunting_query(self, query): ...
    @property
    def alerts(self) -> AlertCollection: ...
    @property
    def alerts_v2(self) -> EntityCollection[Alert]: ...
    @property
    def cases(self): ...
    @property
    def attack_simulation(self): ...
    @property
    def incidents(self) -> EntityCollection[Incident]: ...
    @property
    def secure_score_control_profiles(self): ...
    @property
    def triggers(self): ...
    @property
    def threat_intelligence(self): ...
    def get_property(self, name, default_value: Incomplete | None = None): ...
    @property
    def entity_type_name(self) -> str: ...
