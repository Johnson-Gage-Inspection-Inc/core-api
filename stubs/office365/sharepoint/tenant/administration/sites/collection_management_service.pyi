from office365.runtime.client_object import ClientObject as ClientObject
from office365.runtime.client_result import ClientResult as ClientResult
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath
from office365.runtime.queries.service_operation import ServiceOperationQuery as ServiceOperationQuery
from office365.sharepoint.tenant.administration.sites.creation_source import SiteCreationSource as SiteCreationSource

class SiteCollectionManagementService(ClientObject):
    def __init__(self, context) -> None: ...
    def export_csv_file(self, view_xml): ...
    def get_site_creation_source(self): ...
