from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class MoveCopyOptions(ClientValue):
    KeepBoth: Incomplete
    ResetAuthorAndCreatedOnCopy: Incomplete
    RetainEditorAndModifiedOnMove: Incomplete
    ShouldBypassSharedLocks: Incomplete
    def __init__(self, keep_both: bool = True, reset_author_and_created_on_copy: bool = False, retain_editor_and_modified_on_move: bool = False, should_bypass_shared_locks: bool = False) -> None: ...
    @property
    def entity_type_name(self): ...
