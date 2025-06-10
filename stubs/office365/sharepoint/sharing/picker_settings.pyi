from office365.sharepoint.entity import Entity as Entity
from office365.sharepoint.ui.applicationpages.peoplepicker.query_settings import (
    PeoplePickerQuerySettings as PeoplePickerQuerySettings,
)

class PickerSettings(Entity):
    @property
    def allow_email_addresses(self): ...
    @property
    def allow_only_email_addresses(self): ...
    @property
    def query_settings(self): ...
