from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class ChangeQuery(ClientValue):
    Item: Incomplete
    Alert: Incomplete
    ContentType: Incomplete
    Web: Incomplete
    Site: Incomplete
    List: Incomplete
    Activity: Incomplete
    File: Incomplete
    Folder: Incomplete
    User: Incomplete
    Group: Incomplete
    View: Incomplete
    Add: Incomplete
    Update: Incomplete
    SystemUpdate: Incomplete
    ChangeTokenStart: Incomplete
    ChangeTokenEnd: Incomplete
    DeleteObject: Incomplete
    RoleAssignmentAdd: Incomplete
    RoleAssignmentDelete: Incomplete
    FetchLimit: Incomplete
    def __init__(self, alert: bool = False, site: bool = False, web: bool = False, list_: bool = False, item: bool = False, activity: bool = False, file: bool = False, folder: bool = False, user: bool = False, group: bool = False, view: bool = False, content_type: bool = False, add: bool = True, update: bool = True, system_update: bool = True, delete_object: bool = True, role_assignment_add: bool = True, role_assignment_delete: bool = True, change_token_start: Incomplete | None = None, change_token_end: Incomplete | None = None, fetch_limit: Incomplete | None = None) -> None: ...
    @property
    def entity_type_name(self): ...
