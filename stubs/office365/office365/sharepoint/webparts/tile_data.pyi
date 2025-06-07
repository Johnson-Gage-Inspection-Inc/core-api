from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue
from office365.runtime.types.collections import StringCollection as StringCollection

class TileData(ClientValue):
    BackgroundCollageImageLocations: Incomplete
    BackgroundImageLocation: Incomplete
    BackgroundImageRendersAsIcon: Incomplete
    BodyText: Incomplete
    Description: Incomplete
    HoverDisabled: Incomplete
    ID: Incomplete
    def __init__(
        self,
        background_collage_image_locations: Incomplete | None = None,
        background_image_location: Incomplete | None = None,
        background_image_renders_as_icon: Incomplete | None = None,
        body_text: Incomplete | None = None,
        description: Incomplete | None = None,
        hover_disabled: Incomplete | None = None,
        id_: Incomplete | None = None,
    ) -> None: ...
