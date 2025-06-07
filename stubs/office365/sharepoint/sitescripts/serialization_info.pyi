from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue
from office365.runtime.types.collections import StringCollection as StringCollection

class SiteScriptSerializationInfo(ClientValue):
    IncludeBranding: Incomplete
    IncludedLists: Incomplete
    IncludeLinksToExportedItems: Incomplete
    IncludeRegionalSettings: Incomplete
    IncludeSiteExternalSharingCapability: Incomplete
    IncludeTheme: Incomplete
    def __init__(self, include_branding: Incomplete | None = None, included_lists: Incomplete | None = None, include_links_to_exported_items: Incomplete | None = None, include_regional_settings: Incomplete | None = None, include_site_external_sharing_capability: Incomplete | None = None, include_theme: Incomplete | None = None) -> None: ...
    @property
    def entity_type_name(self): ...
