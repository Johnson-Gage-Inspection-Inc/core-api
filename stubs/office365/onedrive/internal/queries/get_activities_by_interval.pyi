from _typeshed import Incomplete
from office365.entity_collection import EntityCollection as EntityCollection
from office365.onedrive.analytics.item_activity_stat import (
    ItemActivityStat as ItemActivityStat,
)
from office365.runtime.queries.function import FunctionQuery as FunctionQuery

def build_get_activities_by_interval_query(
    binding_type,
    start_dt: Incomplete | None = None,
    end_dt: Incomplete | None = None,
    interval: Incomplete | None = None,
): ...
