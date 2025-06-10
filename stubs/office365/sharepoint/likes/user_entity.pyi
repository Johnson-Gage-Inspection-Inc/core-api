from office365.sharepoint.entity import Entity as Entity

class UserEntity(Entity):
    @property
    def creation_date(self) -> str | None: ...
    @property
    def email(self) -> str | None: ...
