from office365.outlook.calendar.place import Place as Place

class Room(Place):
    @property
    def audio_device_name(self) -> str | None: ...
    @property
    def building(self) -> str | None: ...
