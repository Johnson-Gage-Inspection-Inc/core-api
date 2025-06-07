from office365.directory.identitygovernance.accessreview.set import AccessReviewSet as AccessReviewSet
from office365.directory.identitygovernance.appconsent.approval_route import AppConsentApprovalRoute as AppConsentApprovalRoute
from office365.directory.identitygovernance.entitlementmanagement.entitlement_management import EntitlementManagement as EntitlementManagement
from office365.directory.identitygovernance.privilegedaccess.root import PrivilegedAccessRoot as PrivilegedAccessRoot
from office365.directory.identitygovernance.termsofuse.container import TermsOfUseContainer as TermsOfUseContainer
from office365.entity import Entity as Entity
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath

class IdentityGovernance(Entity):
    @property
    def app_consent(self): ...
    @property
    def access_reviews(self): ...
    @property
    def privileged_access(self): ...
    @property
    def terms_of_use(self): ...
    @property
    def entitlement_management(self): ...
