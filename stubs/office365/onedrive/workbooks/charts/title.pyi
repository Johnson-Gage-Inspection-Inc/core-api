from office365.entity import Entity as Entity
from office365.onedrive.workbooks.charts.title_format import WorkbookChartTitleFormat as WorkbookChartTitleFormat
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath

class WorkbookChartTitle(Entity):
    @property
    def format(self): ...
