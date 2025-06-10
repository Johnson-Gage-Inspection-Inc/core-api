from _typeshed import Incomplete
from office365.directory.permissions.identity import Identity as Identity
from office365.directory.permissions.identity_set import IdentitySet as IdentitySet
from office365.onedrive.permissions.sharepoint_identity import (
    SharePointIdentity as SharePointIdentity,
)

class SharePointIdentitySet(IdentitySet):
    group: Incomplete
    siteGroup: Incomplete
    siteUser: Incomplete
    def __init__(self, group=..., site_group=..., site_user=...) -> None: ...
