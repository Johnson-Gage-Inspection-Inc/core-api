from _typeshed import Incomplete
from office365.entity import Entity as Entity
from office365.entity_collection import EntityCollection as EntityCollection
from office365.onedrive.workbooks.charts.axes import (
    WorkbookChartAxes as WorkbookChartAxes,
)
from office365.onedrive.workbooks.charts.data_labels import (
    WorkbookChartDataLabels as WorkbookChartDataLabels,
)
from office365.onedrive.workbooks.charts.legend.legend import (
    WorkbookChartLegend as WorkbookChartLegend,
)
from office365.onedrive.workbooks.charts.series.series import (
    WorkbookChartSeries as WorkbookChartSeries,
)
from office365.onedrive.workbooks.charts.title import (
    WorkbookChartTitle as WorkbookChartTitle,
)
from office365.runtime.client_result import ClientResult as ClientResult
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath
from office365.runtime.queries.function import FunctionQuery as FunctionQuery
from office365.runtime.queries.service_operation import (
    ServiceOperationQuery as ServiceOperationQuery,
)

class WorkbookChart(Entity):
    def image(
        self, width: Incomplete | None = None, height: Incomplete | None = None
    ): ...
    def set_data(self, source_data, series_by): ...
    def set_position(self, start_cell, end_cell): ...
    @property
    def axes(self): ...
    @property
    def data_labels(self): ...
    @property
    def legend(self): ...
    @property
    def series(self): ...
    @property
    def title(self): ...
    @property
    def worksheet(self): ...
    def get_property(self, name, default_value: Incomplete | None = None): ...
