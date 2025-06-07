from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class TenantAppInformation(ClientValue):
    AppPrincipalId: Incomplete
    AppWebFullUrl: Incomplete
    CreationTime: Incomplete
    def __init__(self, app_principal_id: Incomplete | None = None, app_web_full_url: Incomplete | None = None, creation_time: Incomplete | None = None) -> None: ...
