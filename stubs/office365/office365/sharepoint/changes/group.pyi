from office365.sharepoint.changes.change import Change as Change

class ChangeGroup(Change):
    @property
    def group_id(self) -> int | None: ...
