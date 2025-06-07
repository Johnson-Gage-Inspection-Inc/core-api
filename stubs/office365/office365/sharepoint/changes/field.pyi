from office365.sharepoint.changes.change import Change as Change

class ChangeField(Change):
    @property
    def field_id(self) -> str | None: ...
