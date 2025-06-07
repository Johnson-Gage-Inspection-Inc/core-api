from office365.directory.security.alerts.evidence import AlertEvidence as AlertEvidence
from office365.directory.security.alerts.history_state import AlertHistoryState as AlertHistoryState
from office365.entity import Entity as Entity
from office365.runtime.client_value_collection import ClientValueCollection as ClientValueCollection

class Alert(Entity):
    @property
    def actor_display_name(self) -> str | None: ...
    @property
    def alert_policy_id(self) -> str | None: ...
    @property
    def evidence(self): ...
    @property
    def history_states(self): ...
