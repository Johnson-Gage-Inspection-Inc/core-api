from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue
from office365.runtime.client_value_collection import ClientValueCollection as ClientValueCollection
from office365.sharepoint.marketplace.corporatecuratedgallery.addins.permission_failed_info import SPAddinPermissionFailedInfo as SPAddinPermissionFailedInfo
from office365.sharepoint.marketplace.corporatecuratedgallery.addins.permission_info import SPAddinPermissionInfo as SPAddinPermissionInfo

class SPAddinPermissionResponse(ClientValue):
    addinPermissions: Incomplete
    failedAddins: Incomplete
    def __init__(self, addin_permissions: Incomplete | None = None, failed_addins: Incomplete | None = None) -> None: ...
    @property
    def entity_type_name(self): ...
