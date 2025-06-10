from office365.sharepoint.changes.change import Change as Change

class ChangeAlert(Change):
    @property
    def alert_id(self) -> str | None: ...
