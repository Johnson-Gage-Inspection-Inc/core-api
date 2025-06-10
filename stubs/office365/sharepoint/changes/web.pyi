from office365.sharepoint.changes.change import Change as Change

class ChangeWeb(Change):
    @property
    def web_id(self) -> str | None: ...
