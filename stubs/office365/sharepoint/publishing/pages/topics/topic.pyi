from office365.sharepoint.publishing.pages.page import SitePage as SitePage

class TopicSitePage(SitePage):
    @property
    def entity_id(self): ...
    @property
    def entity_type(self): ...
