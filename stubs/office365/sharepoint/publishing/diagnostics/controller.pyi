from office365.runtime.client_result import ClientResult as ClientResult
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath
from office365.runtime.queries.service_operation import ServiceOperationQuery as ServiceOperationQuery
from office365.sharepoint.entity import Entity as Entity
from office365.sharepoint.publishing.diagnostics.page_diagnostics import PageDiagnostics as PageDiagnostics

class PageDiagnosticsController(Entity):
    def __init__(self, context) -> None: ...
    def by_page(self, page_relative_file_path): ...
    @property
    def entity_type_name(self): ...
