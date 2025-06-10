from office365.runtime.client_value_collection import (
    ClientValueCollection as ClientValueCollection,
)
from office365.sharepoint.entity import Entity as Entity
from office365.sharepoint.sitehealth.result import SiteHealthResult as SiteHealthResult

class SiteHealthSummary(Entity):
    @property
    def failed_error_count(self) -> int | None: ...
    @property
    def failed_warning_count(self) -> int | None: ...
    @property
    def passed_count(self) -> int | None: ...
    @property
    def results(self): ...
    @property
    def entity_type_name(self): ...
