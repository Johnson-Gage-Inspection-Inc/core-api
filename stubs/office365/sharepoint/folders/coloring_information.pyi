from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class FolderColors:
    Yellow: str
    Grey: str
    DarkRed: str
    LightRed: str
    DarkOrange: str
    LightOrange: str
    DarkGreen: str
    LightGreen: str
    DarkTeal: str
    LightTeal: str
    DarkBlue: str
    LightBlue: str
    DarkPurple: str
    LightPurple: str
    DarkPink: str
    LightPink: str

class FolderColoringInformation(ClientValue):
    ColorHex: Incomplete
    ColorTag: Incomplete
    Emoji: Incomplete
    def __init__(
        self,
        color_hex: Incomplete | None = None,
        color_tag: Incomplete | None = None,
        emoji: Incomplete | None = None,
    ) -> None: ...
    @property
    def entity_type_name(self): ...
