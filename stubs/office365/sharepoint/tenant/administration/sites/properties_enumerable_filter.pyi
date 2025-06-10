from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class SitePropertiesEnumerableFilter(ClientValue):
    ArchivedBy: Incomplete
    Filter: Incomplete
    GroupIdDefined: Incomplete
    IncludeDetail: Incomplete
    IncludePersonalSite: Incomplete
    StartIndex: Incomplete
    Template: Incomplete
    ArchivedTime: Incomplete
    ArchiveStatus: Incomplete
    def __init__(
        self,
        _filter,
        start_index: Incomplete | None = None,
        include_detail: Incomplete | None = None,
        include_personal_site: Incomplete | None = None,
        group_id_defined: Incomplete | None = None,
        template: Incomplete | None = None,
        archived_by: Incomplete | None = None,
        archived_time: Incomplete | None = None,
        archive_status: Incomplete | None = None,
    ) -> None: ...
    @property
    def entity_type_name(self): ...
