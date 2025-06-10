from office365.sharepoint.entity import Entity as Entity

class TeamChannel(Entity):
    @property
    def folder_id(self) -> str | None: ...
    @property
    def group_id(self) -> str | None: ...
