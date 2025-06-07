from _typeshed import Incomplete
from office365.directory.security.attacksimulations.report_overview import (
    SimulationReportOverview as SimulationReportOverview,
)
from office365.directory.security.attacksimulations.users.details import (
    UserSimulationDetails as UserSimulationDetails,
)
from office365.runtime.client_value import ClientValue as ClientValue
from office365.runtime.client_value_collection import (
    ClientValueCollection as ClientValueCollection,
)

class SimulationReport(ClientValue):
    overview: Incomplete
    simulationUsers: Incomplete
    def __init__(
        self, overview=..., simulation_users: Incomplete | None = None
    ) -> None: ...
