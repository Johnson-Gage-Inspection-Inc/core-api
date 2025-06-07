from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue
from office365.runtime.client_value_collection import ClientValueCollection as ClientValueCollection
from office365.sharepoint.sharing.link_info import LinkInfo as LinkInfo
from office365.sharepoint.utilities.principal_info import PrincipalInfo as PrincipalInfo

class PermissionCollection(ClientValue):
    appConsentPrincipals: Incomplete
    hasInheritedLinks: Incomplete
    links: Incomplete
    principals: Incomplete
    siteAdmins: Incomplete
    totalNumberOfPrincipals: Incomplete
    def __init__(self, app_consent_principals: Incomplete | None = None, has_inherited_links: Incomplete | None = None, links: Incomplete | None = None, principals: Incomplete | None = None, site_admins: Incomplete | None = None, total_number_of_principals: Incomplete | None = None) -> None: ...
    @property
    def entity_type_name(self): ...
