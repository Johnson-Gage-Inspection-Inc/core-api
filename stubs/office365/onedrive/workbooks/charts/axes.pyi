from _typeshed import Incomplete
from office365.entity import Entity as Entity
from office365.onedrive.workbooks.charts.axis import (
    WorkbookChartAxis as WorkbookChartAxis,
)
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath

class WorkbookChartAxes(Entity):
    @property
    def category_axis(self): ...
    @property
    def series_axis(self): ...
    @property
    def value_axis(self): ...
    def get_property(self, name, default_value: Incomplete | None = None): ...
