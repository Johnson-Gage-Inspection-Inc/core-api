from office365.directory.identitygovernance.appconsent.request_collection import (
    AppConsentRequestCollection as AppConsentRequestCollection,
)
from office365.entity import Entity as Entity
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath

class AppConsentApprovalRoute(Entity):
    @property
    def app_consent_requests(self): ...
