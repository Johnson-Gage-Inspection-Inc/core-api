from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue
from office365.runtime.client_value_collection import ClientValueCollection as ClientValueCollection
from office365.sharepoint.activities.identity import ActivityIdentity as ActivityIdentity

class SharingFacet(ClientValue):
    recipients: Incomplete
    sharingType: Incomplete
    def __init__(self, recipients: Incomplete | None = None, sharing_type: Incomplete | None = None) -> None: ...
