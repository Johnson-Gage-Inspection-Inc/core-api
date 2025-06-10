from _typeshed import Incomplete
from office365.onedrive.sharepoint_ids import SharePointIds as SharePointIds
from office365.runtime.client_value import ClientValue as ClientValue

class ItemReference(ClientValue):
    id: Incomplete
    name: Incomplete
    path: Incomplete
    driveId: Incomplete
    driveType: Incomplete
    siteId: Incomplete
    sharepointIds: Incomplete
    shareId: Incomplete
    def __init__(
        self,
        _id: Incomplete | None = None,
        name: Incomplete | None = None,
        path: Incomplete | None = None,
        drive_id: Incomplete | None = None,
        drive_type: Incomplete | None = None,
        site_id: Incomplete | None = None,
        sharepoint_ids=...,
        share_id: Incomplete | None = None,
    ) -> None: ...
