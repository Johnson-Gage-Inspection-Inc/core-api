from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue
from office365.sharepoint.directory.provider.alternate_id_data import AlternateIdData as AlternateIdData
from office365.sharepoint.directory.provider.session_data import DirectorySessionData as DirectorySessionData

class DirectoryObjectData(ClientValue):
    AlternateId: Incomplete
    AttributeExpirationTimes: Incomplete
    ChangeMarker: Incomplete
    DirectoryObjectSubType: Incomplete
    DirectoryObjectType: Incomplete
    DirectorySessionData: Incomplete
    Id: Incomplete
    IsNew: Incomplete
    LastModifiedTime: Incomplete
    TenantContextId: Incomplete
    Version: Incomplete
    def __init__(self, alternate_id=..., attribute_expiration_times: Incomplete | None = None, change_marker: Incomplete | None = None, directory_object_sub_type: Incomplete | None = None, directory_object_type: Incomplete | None = None, directory_session_data=..., id_: Incomplete | None = None, is_new: Incomplete | None = None, last_modified_time: Incomplete | None = None, tenant_context_id: Incomplete | None = None, version: Incomplete | None = None) -> None: ...
    @property
    def entity_type_name(self): ...
