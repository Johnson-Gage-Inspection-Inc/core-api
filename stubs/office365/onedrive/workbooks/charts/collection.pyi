from _typeshed import Incomplete
from office365.entity_collection import EntityCollection as EntityCollection
from office365.onedrive.workbooks.charts.chart import WorkbookChart as WorkbookChart

class WorkbookChartCollection(EntityCollection[WorkbookChart]):
    def __init__(self, context, resource_path: Incomplete | None = None) -> None: ...
