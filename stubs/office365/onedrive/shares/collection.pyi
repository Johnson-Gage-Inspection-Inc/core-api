from _typeshed import Incomplete
from office365.entity_collection import EntityCollection as EntityCollection
from office365.onedrive.internal.paths.shared import SharedPath as SharedPath
from office365.onedrive.shares.drive_item import SharedDriveItem as SharedDriveItem

class SharesCollection(EntityCollection[SharedDriveItem]):
    def __init__(self, context, resource_path: Incomplete | None = None) -> None: ...
    def by_url(self, url: str) -> SharedDriveItem: ...
