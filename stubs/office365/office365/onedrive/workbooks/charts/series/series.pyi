from office365.entity import Entity as Entity
from office365.entity_collection import EntityCollection as EntityCollection
from office365.onedrive.workbooks.charts.point import (
    WorkbookChartPoint as WorkbookChartPoint,
)
from office365.onedrive.workbooks.charts.series.format import (
    WorkbookChartSeriesFormat as WorkbookChartSeriesFormat,
)
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath

class WorkbookChartSeries(Entity):
    @property
    def format(self): ...
    @property
    def points(self): ...
