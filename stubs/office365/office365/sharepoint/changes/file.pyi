from office365.sharepoint.changes.change import Change as Change

class ChangeFile(Change):
    @property
    def unique_id(self) -> str | None: ...
    @property
    def web_id(self) -> str | None: ...
