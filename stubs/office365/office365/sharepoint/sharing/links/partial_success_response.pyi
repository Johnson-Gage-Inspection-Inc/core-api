from office365.sharepoint.sharing.links.share_response import (
    ShareLinkResponse as ShareLinkResponse,
)

class ShareLinkPartialSuccessResponse(ShareLinkResponse):
    @property
    def entity_type_name(self): ...
