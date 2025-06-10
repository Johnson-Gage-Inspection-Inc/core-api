from office365.runtime.client_value import ClientValue as ClientValue
from office365.sharepoint.publishing.pages.fields_data import (
    SitePageFieldsData as SitePageFieldsData,
)

class CampaignPublicationMailDraftData(ClientValue):
    @property
    def entity_type_name(self): ...

class CampaignPublicationFieldsData(SitePageFieldsData):
    @property
    def entity_type_name(self): ...
