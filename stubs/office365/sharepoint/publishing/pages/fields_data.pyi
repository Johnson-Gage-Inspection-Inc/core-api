from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class SitePageFieldsData(ClientValue):
    BannerImageUrl: Incomplete
    CanvasContent1: Incomplete
    CanvasJson1: Incomplete
    Title: Incomplete
    TopicHeader: Incomplete
    PublishStartDate: Incomplete
    def __init__(self, title: Incomplete | None = None, banner_image_url: Incomplete | None = None, canvas_content: Incomplete | None = None, topic_header: Incomplete | None = None, publish_start_date: Incomplete | None = None) -> None: ...
    @property
    def entity_type_name(self): ...
