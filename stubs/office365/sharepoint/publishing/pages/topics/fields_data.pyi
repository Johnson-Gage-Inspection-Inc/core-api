from _typeshed import Incomplete
from office365.sharepoint.publishing.pages.fields_data import SitePageFieldsData as SitePageFieldsData

class TopicPageFieldsData(SitePageFieldsData):
    EntityId: Incomplete
    EntityRelations: Incomplete
    def __init__(self, entity_id: Incomplete | None = None, entity_relations: Incomplete | None = None) -> None: ...
    @property
    def entity_type_name(self): ...
