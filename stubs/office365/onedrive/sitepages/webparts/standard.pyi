from office365.onedrive.sitepages.webparts.data import WebPartData as WebPartData
from office365.onedrive.sitepages.webparts.web_part import WebPart as WebPart

class StandardWebPart(WebPart):
    @property
    def data(self) -> WebPartData | None: ...
