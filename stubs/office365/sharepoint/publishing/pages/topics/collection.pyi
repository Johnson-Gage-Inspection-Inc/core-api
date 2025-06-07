from _typeshed import Incomplete
from office365.sharepoint.entity_collection import EntityCollection as EntityCollection
from office365.sharepoint.publishing.pages.topics.topic import TopicSitePage as TopicSitePage

class TopicPageCollection(EntityCollection[TopicSitePage]):
    def __init__(self, context, resource_path: Incomplete | None = None) -> None: ...
