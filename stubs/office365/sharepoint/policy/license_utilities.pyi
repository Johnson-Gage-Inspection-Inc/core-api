from _typeshed import Incomplete
from office365.runtime.client_result import ClientResult as ClientResult
from office365.runtime.queries.service_operation import ServiceOperationQuery as ServiceOperationQuery
from office365.sharepoint.entity import Entity as Entity

class PolicyLicenseUtilities(Entity):
    @staticmethod
    def check_tenant_m365_copilot_business_chat_license(context, return_type: Incomplete | None = None): ...
    @property
    def entity_type_name(self): ...
