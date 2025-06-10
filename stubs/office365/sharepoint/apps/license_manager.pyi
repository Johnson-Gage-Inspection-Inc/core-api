from office365.runtime.client_result import ClientResult as ClientResult
from office365.runtime.queries.service_operation import (
    ServiceOperationQuery as ServiceOperationQuery,
)
from office365.sharepoint.apps.license_collection import (
    AppLicenseCollection as AppLicenseCollection,
)
from office365.sharepoint.entity import Entity as Entity

class SPAppLicenseManager(Entity):
    def check_license(self, product_id): ...
