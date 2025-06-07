from office365.sharepoint.changes.change import Change as Change

class ChangeUser(Change):
    @property
    def activate(self) -> bool | None: ...
    @property
    def user_id(self) -> str | None: ...
