from office365.sharepoint.changes.change import Change as Change

class ChangeContentType(Change):
    @property
    def content_type_id(self) -> str | None: ...
