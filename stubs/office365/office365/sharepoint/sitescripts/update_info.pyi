from office365.sharepoint.sitescripts.creation_info import (
    SiteScriptCreationInfo as SiteScriptCreationInfo,
)

class SiteScriptUpdateInfo(SiteScriptCreationInfo):
    @property
    def entity_type_name(self): ...
