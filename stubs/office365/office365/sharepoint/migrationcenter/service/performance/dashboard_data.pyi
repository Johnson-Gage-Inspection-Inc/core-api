from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue
from office365.runtime.client_value_collection import (
    ClientValueCollection as ClientValueCollection,
)
from office365.runtime.types.collections import StringCollection as StringCollection
from office365.sharepoint.migrationcenter.service.performance.throughput_data import (
    ThroughputData as ThroughputData,
)

class PerformanceDashboardData(ClientValue):
    BottleneckList: Incomplete
    RecommendationList: Incomplete
    ThroughputTrend: Incomplete
    def __init__(
        self,
        bottleneck_list: Incomplete | None = None,
        recommendation_list: Incomplete | None = None,
        throughput_trend: Incomplete | None = None,
    ) -> None: ...
    @property
    def entity_type_name(self): ...
