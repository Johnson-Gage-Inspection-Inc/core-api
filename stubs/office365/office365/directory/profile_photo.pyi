from office365.entity import Entity as Entity

class ProfilePhoto(Entity):
    @property
    def height(self) -> int | None: ...
    @property
    def width(self) -> int | None: ...
